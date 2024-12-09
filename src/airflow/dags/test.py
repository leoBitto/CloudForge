from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="test_postgres_connections",
    start_date=datetime(2024, 6, 10),
    schedule_interval=None,
    catchup=False
) as dag:

    test_silver = PostgresOperator(
        task_id="test_silver_db",
        postgres_conn_id="postgres_silver",
        sql="SELECT 1;"
    )

    test_gold = PostgresOperator(
        task_id="test_gold_db",
        postgres_conn_id="postgres_gold",
        sql="SELECT 1;"
    )

    test_silver >> test_gold
