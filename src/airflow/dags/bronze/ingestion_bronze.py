from datetime import datetime, timedelta
from airflow.decorators import dag, task
import polars as pl
from deltalake.writer import write_deltalake
import yfinance as yf
import os

DATA_FOLDER = '/opt/airflow/data/'
MISC_FOLDER = os.path.join(DATA_FOLDER, 'misc')
BRONZE_FOLDER = os.path.join(DATA_FOLDER, 'bronze/yfinance')
ENRICHED_PATH = os.path.join(MISC_FOLDER, 'enriched_full.csv')

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='bronze_yfinance_ingestion_delta',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bronze', 'yfinance', 'delta'],
)
def bronze_yfinance():

    @task()
    def read_tickers():
        df = pl.read_csv(ENRICHED_PATH)
        return df['Ticker'].unique().to_list()

    @task()
    def download_to_delta(ticker: str):
        table_path = os.path.join(BRONZE_FOLDER, ticker)
        os.makedirs(table_path, exist_ok=True)

        start_date = '2024-01-01'
        end_date = datetime.now().strftime('%Y-%m-%d')

        # Se la tabella esiste, calcolo la start_date
        if os.path.exists(os.path.join(table_path, '_delta_log')):
            existing = pl.read_delta(table_path)
            if existing.shape[0] > 0:
                last_date = existing.select(pl.col('Date').max()).item()
                start_date = (pl.datetime(last_date) + timedelta(days=1)).strftime('%Y-%m-%d')

        # Scarico
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            return f"Nessun dato nuovo per {ticker}"

        df.reset_index(inplace=True)
        pl_df = pl.from_pandas(df)
        pl_df = pl_df.with_columns([
            pl.lit(ticker).alias("Ticker")
        ])

        # Scrivo in Delta
        write_deltalake(
            table_or_uri=table_path,
            data=pl_df,
            mode="append"
        )

        return f"{ticker}: salvato su Delta da {start_date} a {end_date}"

    tickers = read_tickers()
    download_to_delta.expand(ticker=tickers)

dag = bronze_yfinance()
