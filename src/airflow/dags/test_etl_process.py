from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import pandas as pd

# Definizione dei default args per il DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def extract_from_bronze():
    """Estrae i dati dal database bronze"""
    pg_hook = PostgresHook(postgres_conn_id='postgres_bronze')
    
    sql = """
        SELECT * FROM test_orders 
        WHERE order_date >= %(start_date)s 
        AND order_date < %(end_date)s
    """
    
    # Ottiene la data di esecuzione del DAG
    execution_date = "{{ ds }}"
    next_day = "{{ tomorrow_ds }}"
    
    df = pg_hook.get_pandas_df(
        sql, 
        parameters={
            'start_date': execution_date,
            'end_date': next_day
        }
    )
    
    return df.to_dict('records')

def transform_to_silver(ti):
    """Trasforma i dati e li carica nel database silver"""
    # Recupera i dati estratti
    data = ti.xcom_pull(task_ids='extract_from_bronze')
    df = pd.DataFrame(data)
    
    # Aggrega i dati per data
    daily_summary = df.groupby('order_date').agg({
        'order_id': 'count',
        'total_amount': 'sum'
    }).reset_index()
    
    daily_summary.columns = ['order_date', 'total_orders', 'daily_revenue']
    
    # Carica i dati nel database silver
    pg_hook = PostgresHook(postgres_conn_id='postgres_silver')
    
    # Crea la tabella se non esiste
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS test_orders_daily (
            order_date DATE PRIMARY KEY,
            total_orders INTEGER,
            daily_revenue DECIMAL(12,2)
        )
    """
    pg_hook.run(create_table_sql)
    
    # Inserisce i dati
    pg_hook.insert_rows(
        table='test_orders_daily',
        rows=daily_summary.to_dict('records'),
        target_fields=['order_date', 'total_orders', 'daily_revenue'],
        replace=True,
        replace_index=['order_date']
    )
    
    return daily_summary.to_dict('records')

def load_to_gold(ti):
    """Aggrega ulteriormente i dati e li carica nel database gold"""
    # Recupera i dati dal silver
    pg_hook_silver = PostgresHook(postgres_conn_id='postgres_silver')
    
    sql = """
        SELECT * FROM test_orders_daily
        WHERE order_date >= %(start_date)s 
        AND order_date < %(end_date)s
    """
    
    execution_date = "{{ ds }}"
    next_day = "{{ tomorrow_ds }}"
    
    df = pg_hook_silver.get_pandas_df(
        sql,
        parameters={
            'start_date': execution_date,
            'end_date': next_day
        }
    )
    
    # Calcola metriche aggregate
    summary = {
        'date': execution_date,
        'total_orders': int(df['total_orders'].sum()),
        'total_revenue': float(df['daily_revenue'].sum()),
        'avg_order_value': float(df['daily_revenue'].sum() / df['total_orders'].sum()) if df['total_orders'].sum() > 0 else 0
    }
    
    # Carica nel database gold
    pg_hook_gold = PostgresHook(postgres_conn_id='postgres_gold')
    
    # Crea la tabella se non esiste
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS test_orders_summary (
            date DATE PRIMARY KEY,
            total_orders INTEGER,
            total_revenue DECIMAL(12,2),
            avg_order_value DECIMAL(10,2)
        )
    """
    pg_hook_gold.run(create_table_sql)
    
    # Inserisce i dati
    pg_hook_gold.insert_rows(
        table='test_orders_summary',
        rows=[summary],
        target_fields=['date', 'total_orders', 'total_revenue', 'avg_order_value'],
        replace=True,
        replace_index=['date']
    )

# Creazione del DAG
with DAG(
    'test_etl_process',
    default_args=default_args,
    description='ETL process for testing',
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    # Task per estrarre i dati dal bronze
    extract_task = PythonOperator(
        task_id='extract_from_bronze',
        python_callable=extract_from_bronze
    )
    
    # Task per trasformare e caricare i dati nel silver
    transform_task = PythonOperator(
        task_id='transform_to_silver',
        python_callable=transform_to_silver
    )
    
    # Task per aggregare e caricare i dati nel gold
    load_task = PythonOperator(
        task_id='load_to_gold',
        python_callable=load_to_gold
    )
    
    # Definizione del flusso
    extract_task >> transform_task >> load_task