import pytest
import subprocess
import time
import psycopg2
from psycopg2 import OperationalError

# Test database connectivity for both silver and gold databases
def test_postgres_silver_connection():
    time.sleep(10)
    try:
        conn = psycopg2.connect(
            dbname="silver_db", 
            user="silver_user", 
            password="silver_password", 
            host="postgres-silver", 
            port="5432"
        )
        conn.close()
    except OperationalError as e:
        pytest.fail(f"Silver database connection failed: {e}")

def test_postgres_gold_connection():
    time.sleep(10)
    try:
        conn = psycopg2.connect(
            dbname="gold_db", 
            user="gold_user", 
            password="gold_password", 
            host="postgres-gold", 
            port="5432"
        )
        conn.close()
    except OperationalError as e:
        pytest.fail(f"Gold database connection failed: {e}")

# Test the migration process for silver database
def test_migrations_silver():
    try:
        result = subprocess.run(
            ["docker", "compose", "exec", "-T", "django-app", "python", "manage.py", "makemigrations"],
            capture_output=True, text=True
        )
        if "No changes detected" not in result.stdout:
            pytest.fail(f"Migrations for silver database failed: {result.stderr}")
        
        result = subprocess.run(
            ["docker", "compose", "exec", "-T", "django-app", "python", "manage.py", "migrate", "--database=silver"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            pytest.fail(f"Migration failed for silver database: {result.stderr}")
    except Exception as e:
        pytest.fail(f"Error during migration for silver database: {e}")

# Test the migration process for gold database (simplified)
def test_migrations_gold():
    try:
        result = subprocess.run(
            ["docker", "compose", "exec", "-T", "django-app", "python", "manage.py", "makemigrations"],
            capture_output=True, text=True
        )
        if "No changes detected" not in result.stdout:
            pytest.fail(f"Migrations for gold database failed: {result.stderr}")
        
        result = subprocess.run(
            ["docker", "compose", "exec", "-T", "django-app", "python", "manage.py", "migrate", "--database=gold"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            pytest.fail(f"Migration failed for gold database: {result.stderr}")
    except Exception as e:
        pytest.fail(f"Error during migration for gold database: {e}")