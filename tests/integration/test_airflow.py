import pytest
from airflow.models import DagBag
from airflow.utils.session import create_session
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Funzioni di utility per la connessione ai database
def get_db_connection(db_type):
    """Crea una connessione al database specificato"""
    db_params = {
        'bronze': {
            'dbname': os.getenv('POSTGRES_DB_BRONZE', 'bronze_db'),
            'user': os.getenv('POSTGRES_USER_BRONZE', 'bronze_user'),
            'password': os.getenv('POSTGRES_PASSWORD_BRONZE', 'bronze_pass'),
            'host': 'postgres-bronze'
        },
        'silver': {
            'dbname': os.getenv('POSTGRES_DB_SILVER', 'silver_db'),
            'user': os.getenv('POSTGRES_USER_SILVER', 'silver_user'),
            'password': os.getenv('POSTGRES_PASSWORD_SILVER', 'silver_pass'),
            'host': 'postgres-silver'
        },
        'gold': {
            'dbname': os.getenv('POSTGRES_DB_GOLD', 'gold_db'),
            'user': os.getenv('POSTGRES_USER_GOLD', 'gold_user'),
            'password': os.getenv('POSTGRES_PASSWORD_GOLD', 'gold_pass'),
            'host': 'postgres-gold'
        }
    }
    
    params = db_params[db_type]
    return psycopg2.connect(**params)

# Fixture per preparare i dati di test
@pytest.fixture(scope="module")
def setup_test_data():
    # Inserisce dati di test nel database bronze
    conn = get_db_connection('bronze')
    cur = conn.cursor()
    
    # Crea una tabella di test nel database bronze
    cur.execute("""
        CREATE TABLE IF NOT EXISTS test_orders (
            order_id SERIAL PRIMARY KEY,
            customer_id INTEGER,
            order_date DATE,
            total_amount DECIMAL(10,2)
        )
    """)
    
    # Inserisce alcuni dati di test
    cur.execute("""
        INSERT INTO test_orders (customer_id, order_date, total_amount)
        VALUES 
            (1, '2024-01-01', 100.00),
            (2, '2024-01-01', 150.00),
            (1, '2024-01-02', 200.00)
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    
    yield
    
    # Pulizia dopo i test
    for db_type in ['bronze', 'silver', 'gold']:
        conn = get_db_connection(db_type)
        cur = conn.cursor()
        if db_type == 'bronze':
            cur.execute("DROP TABLE IF EXISTS test_orders")
        elif db_type == 'silver':
            cur.execute("DROP TABLE IF EXISTS test_orders_daily")
        elif db_type == 'gold':
            cur.execute("DROP TABLE IF EXISTS test_orders_summary")
        conn.commit()
        cur.close()
        conn.close()

# Test del DAG
def test_etl_dag(setup_test_data):
    dag_id = 'test_etl_process'
    dagbag = DagBag(dag_folder='/opt/airflow/dags', include_examples=False)
    
    # Verifica che il DAG sia stato caricato correttamente
    assert dag_id in dagbag.dags
    assert len(dagbag.import_errors) == 0
    
    # Ottiene il DAG
    dag = dagbag.get_dag(dag_id)
    
    # Esegue il DAG
    execution_date = days_ago(1)
    dag.clear(start_date=execution_date)
    dag.run(start_date=execution_date, end_date=execution_date)
    
    # Verifica i risultati nel database silver
    conn_silver = get_db_connection('silver')
    cur_silver = conn_silver.cursor(cursor_factory=RealDictCursor)
    cur_silver.execute("SELECT * FROM test_orders_daily")
    silver_results = cur_silver.fetchall()
    
    # Verifica che i dati siano stati aggregati correttamente nel silver
    assert len(silver_results) > 0
    assert 'order_date' in silver_results[0]
    assert 'total_orders' in silver_results[0]
    
    # Verifica i risultati nel database gold
    conn_gold = get_db_connection('gold')
    cur_gold = conn_gold.cursor(cursor_factory=RealDictCursor)
    cur_gold.execute("SELECT * FROM test_orders_summary")
    gold_results = cur_gold.fetchall()
    
    # Verifica che i dati siano stati aggregati correttamente nel gold
    assert len(gold_results) > 0
    assert 'total_revenue' in gold_results[0]
    
    # Chiude le connessioni
    cur_silver.close()
    conn_silver.close()
    cur_gold.close()
    conn_gold.close()