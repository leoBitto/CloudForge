import pytest
from airflow.hooks.postgres_hook import PostgresHook

def test_airflow_postgres_bronze_connection():
    """
    Testa che la connessione a PostgreSQL Bronze tramite Airflow sia funzionante e verifica la lettura/scrittura.
    """
    try:
        hook = PostgresHook(postgres_conn_id='postgres_bronze')
        conn = hook.get_conn()
        cursor = conn.cursor()
        
        # Test di scrittura
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, value TEXT);")
        cursor.execute("INSERT INTO test_table (value) VALUES ('test_value');")
        conn.commit()
        
        # Test di lettura
        cursor.execute("SELECT value FROM test_table WHERE value='test_value';")
        result = cursor.fetchone()
        assert result[0] == 'test_value', f"Query returned unexpected result: {result}"
        
        # Cleanup
        cursor.execute("DROP TABLE test_table;")
        conn.commit()
    except Exception as e:
        pytest.fail(f"Connection to 'postgres_bronze' failed: {e}")

def test_airflow_postgres_silver_connection():
    """
    Testa che la connessione a PostgreSQL Silver tramite Airflow sia funzionante e verifica la lettura/scrittura.
    """
    try:
        hook = PostgresHook(postgres_conn_id='postgres_silver')
        conn = hook.get_conn()
        cursor = conn.cursor()
        
        # Test di scrittura
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, value TEXT);")
        cursor.execute("INSERT INTO test_table (value) VALUES ('test_value');")
        conn.commit()
        
        # Test di lettura
        cursor.execute("SELECT value FROM test_table WHERE value='test_value';")
        result = cursor.fetchone()
        assert result[0] == 'test_value', f"Query returned unexpected result: {result}"
        
        # Cleanup
        cursor.execute("DROP TABLE test_table;")
        conn.commit()
    except Exception as e:
        pytest.fail(f"Connection to 'postgres_silver' failed: {e}")

def test_airflow_postgres_gold_connection():
    """
    Testa che la connessione a PostgreSQL Gold tramite Airflow sia funzionante e verifica la lettura/scrittura.
    """
    try:
        hook = PostgresHook(postgres_conn_id='postgres_gold')
        conn = hook.get_conn()
        cursor = conn.cursor()
        
        # Test di scrittura
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, value TEXT);")
        cursor.execute("INSERT INTO test_table (value) VALUES ('test_value');")
        conn.commit()
        
        # Test di lettura
        cursor.execute("SELECT value FROM test_table WHERE value='test_value';")
        result = cursor.fetchone()
        assert result[0] == 'test_value', f"Query returned unexpected result: {result}"
        
        # Cleanup
        cursor.execute("DROP TABLE test_table;")
        conn.commit()
    except Exception as e:
        pytest.fail(f"Connection to 'postgres_gold' failed: {e}")