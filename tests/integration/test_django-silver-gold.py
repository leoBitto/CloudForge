import pytest
from django.conf import settings
from django.core.management import call_command
from django.db import connections
import sys

def test_print_sys_path():
    """Test di debug per verificare il PYTHONPATH"""
    print("\nPYTHONPATH:", sys.path)

@pytest.fixture(params=["default", "silver", "gold"])
def setup_database(request, django_db_setup, django_db_blocker):
    """
    Fixture che configura il database attivo in base al parametro.
    Usa django_db_setup e django_db_blocker per gestire correttamente le connessioni.
    """
    database_name = request.param
    
    with django_db_blocker.unblock():  # Sblocca esplicitamente l'accesso al DB
        settings.DATABASES['default'] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': f"{database_name}_db",
            'USER': f"{database_name}_user",
            'PASSWORD': f"{database_name}_password",
            'HOST': f"postgres-{database_name}",
            'PORT': "5432",
        }
        
        # Chiudi le connessioni esistenti per applicare le nuove impostazioni
        connections.close_all()
        
        yield database_name
        
        # Cleanup
        connections.close_all()

def test_database_connection(setup_database):
    """
    Testa che la connessione ai database sia funzionante.
    """
    database_name = setup_database
    try:
        with connections[database_name].cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()
            assert result[0] == 1, f"Query returned unexpected result: {result}"
    except Exception as e:
        pytest.fail(f"Connection to '{database_name}' failed: {e}")


def test_migrations(setup_database):
    """
    Test migrations are applied for the configured database.
    """
    database_name = setup_database
    try:
        # Esegui migrate sul database specifico
        call_command("migrate", "--database", database_name, "--no-input", verbosity=1)

        # Verifica l'esistenza della tabella django_migrations
        with connections[database_name].cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_name = 'django_migrations'
                );
            """)
            table_exists = cursor.fetchone()[0]
            assert table_exists, f"django_migrations table does not exist in {database_name} database"

    except Exception as e:
        pytest.fail(f"Migration failed for '{database_name}': {e}")
