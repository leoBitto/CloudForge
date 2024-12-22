import pytest
import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Funzioni di utility per la connessione ai database
def get_db_connection(db_type):
    """Crea una connessione al database specificato"""
    db_params = {
        'bronze': {
            'dbname': os.getenv('BRONZE_POSTGRES_DB', 'bronze_db'),
            'user': os.getenv('BRONZE_POSTGRES_USER', 'bronze_user'),
            'password': os.getenv('BRONZE_POSTGRES_PASSWORD', 'bronze_pass'),
            'host': 'postgres-bronze'
        },
        'silver': {
            'dbname': os.getenv('SILVER_POSTGRES_DB', 'silver_db'),
            'user': os.getenv('SILVER_POSTGRES_USER', 'silver_user'),
            'password': os.getenv('SILVER_POSTGRES_PASSWORD', 'silver_pass'),
            'host': 'postgres-silver'
        },
        'gold': {
            'dbname': os.getenv('GOLD_POSTGRES_DB', 'gold_db'),
            'user': os.getenv('GOLD_POSTGRES_USER', 'gold_user'),
            'password': os.getenv('GOLD_POSTGRES_PASSWORD', 'gold_pass'),
            'host': 'postgres-gold'
        }
    }
    
    params = db_params[db_type]
    return psycopg2.connect(**params)

# Fixture per preparare e pulire i dati di test
@pytest.fixture(scope="module")
def setup_test_data():
    """Crea tabelle e inserisce dati nei database"""
    for db_type in ['bronze', 'silver', 'gold']:
        conn = get_db_connection(db_type)
        cur = conn.cursor()
        
        if db_type == 'bronze':
            cur.execute("""
                CREATE TABLE IF NOT EXISTS bronze_table (
                    id SERIAL PRIMARY KEY,
                    data TEXT
                )
            """)
            cur.execute("""
                INSERT INTO bronze_table (data)
                VALUES ('Sample data for bronze')
                ON CONFLICT DO NOTHING
            """)
        
        elif db_type == 'silver':
            cur.execute("""
                CREATE TABLE IF NOT EXISTS silver_table (
                    id SERIAL PRIMARY KEY,
                    data TEXT
                )
            """)
            cur.execute("""
                INSERT INTO silver_table (data)
                VALUES ('Sample data for silver')
                ON CONFLICT DO NOTHING
            """)
        
        elif db_type == 'gold':
            cur.execute("""
                CREATE TABLE IF NOT EXISTS gold_table (
                    id SERIAL PRIMARY KEY,
                    data TEXT
                )
            """)
            cur.execute("""
                INSERT INTO gold_table (data)
                VALUES ('Sample data for gold')
                ON CONFLICT DO NOTHING
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
            cur.execute("DROP TABLE IF EXISTS bronze_table")
        elif db_type == 'silver':
            cur.execute("DROP TABLE IF EXISTS silver_table")
        elif db_type == 'gold':
            cur.execute("DROP TABLE IF EXISTS gold_table")
        conn.commit()
        cur.close()
        conn.close()

# Test per verificare lettura e scrittura nei database
def test_read_write_databases(setup_test_data):
    for db_type in ['bronze', 'silver', 'gold']:
        conn = get_db_connection(db_type)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Legge i dati dalla tabella
        if db_type == 'bronze':
            cur.execute("SELECT * FROM bronze_table")
        elif db_type == 'silver':
            cur.execute("SELECT * FROM silver_table")
        elif db_type == 'gold':
            cur.execute("SELECT * FROM gold_table")
        
        results = cur.fetchall()
        
        # Verifica che ci sia almeno una riga di dati
        assert len(results) > 0, f"No data found in {db_type} database"
        assert 'data' in results[0], f"Column 'data' not found in {db_type} database"
        
        cur.close()
        conn.close()
