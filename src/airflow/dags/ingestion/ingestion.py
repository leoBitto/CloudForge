from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import yfinance as yf
import pandas as pd
import os

# Configurazione dei parametri di default
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 4, 23)
}

# Funzione per scaricare dati da Yahoo Finance
def download_ticker_data(**kwargs):
    # Parametri
    ticker = kwargs.get('ticker', 'AAPL')
    start_date = kwargs.get('start_date', '2024-01-01')
    end_date = kwargs.get('end_date', datetime.now().strftime('%Y-%m-%d'))
    output_path = kwargs.get('output_path', '/tmp/yfinance_data')
    
    # Crea la directory di output se non esiste
    os.makedirs(output_path, exist_ok=True)
    
    # Download dei dati
    print(f"Scaricando dati per {ticker} dal {start_date} al {end_date}")
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Salvataggio in CSV
    csv_file = f"{output_path}/{ticker}_{start_date}_to_{end_date.replace('-', '_')}.csv"
    data.to_csv(csv_file)
    print(f"Dati salvati in: {csv_file}")
    
    return csv_file

# Creazione della DAG
dag = DAG(
    'yfinance_ticker_download',
    default_args=default_args,
    description='Scarica dati storici di un ticker da Yahoo Finance',
    schedule_interval='@daily',
    catchup=False,
    tags=['finance', 'yahoo', 'data']
)

# Task per scaricare i dati di un ticker specifico
download_task = PythonOperator(
    task_id='download_ticker_data',
    python_callable=download_ticker_data,
    op_kwargs={
        'ticker': 'AAPL',  # Puoi cambiare il ticker qui
        'start_date': '2024-01-01',
        'end_date': datetime.now().strftime('%Y-%m-%d'),
        'output_path': '/tmp/yfinance_data'
    },
    dag=dag
)

# Definizione del flusso delle attività
download_task