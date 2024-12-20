import pytest
from airflow.settings import engine
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import DagBag
from sqlalchemy import text
import requests

# -------- TEST 1: Connessione al database dei metadati -------- #
def test_airflow_metadata_db_connection():
    """
    Check that Airflow can connect to its metadata database.
    Executes a simple SELECT 1 query.
    """
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1, "Failed to connect to Airflow metadata database."

# -------- TEST 2: Connessione ai database bronze, silver, gold -------- #
@pytest.mark.parametrize("conn_id", ["bronze_db", "silver_db", "gold_db"])
def test_airflow_db_connections(conn_id):
    """
    Check that Airflow can connect to bronze, silver, and gold databases.
    """
    hook = PostgresHook(postgres_conn_id=conn_id)
    result = hook.get_first("SELECT 1;")
    assert result is not None and result[0] == 1, f"Failed to connect using {conn_id}."

# -------- TEST 3: Caricamento dei DAG -------- #
def test_dag_loading():
    """
    Ensure that all DAGs load without import errors.
    """
    dag_bag = DagBag(include_examples=False)
    assert len(dag_bag.import_errors) == 0, f"Import errors found: {dag_bag.import_errors}"

# -------- TEST 4: Verifica che il webserver sia raggiungibile -------- #
def test_airflow_webserver():
    """
    Check that the Airflow webserver is reachable and returns a 200 status code.
    """
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        assert response.status_code == 200, "Airflow webserver is not responding correctly."
    except requests.ConnectionError as e:
        pytest.fail(f"Failed to connect to Airflow webserver: {e}")
