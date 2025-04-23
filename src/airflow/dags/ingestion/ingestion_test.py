from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import os

# Funzione per leggere il CSV
def read_csv_file():
    file_path = '/opt/airflow/data/misc/enriched_full.csv'
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File non trovato: {file_path}")
    
    df = pd.read_csv(file_path)
    print("✅ CSV caricato correttamente, ecco le prime righe:")
    print(df.head())
    return df

# Creazione DAG
with DAG(
    dag_id='read_csv_test',
    description='Legge un CSV dalla cartella data/misc',
    schedule_interval=None,  # la fai girare manualmente
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    read_csv = PythonOperator(
        task_id='read_csv',
        python_callable=read_csv_file
    )
