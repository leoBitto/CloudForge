import os
import psycopg2
import pandas as pd
import streamlit as st

# Configurazioni da variabili d'ambiente
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
SQL_HOST = os.getenv("SQL_HOST")
SQL_PORT = os.getenv("SQL_PORT")

DJANGO_API_URL = os.getenv("DJANGO_API_URL")

# Funzione per connettersi al database Postgres
def get_data_from_gold_db():
    try:
        # Connessione al database Postgres
        conn = psycopg2.connect(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=SQL_HOST,
            port=SQL_PORT
        )

        # Query di esempio
        query = "SELECT 1;"
        df = pd.read_sql(query, conn)
        conn.close()

        return df

    except Exception as e:
        st.error(f"Errore nella connessione al database: {e}")
        return None

# Funzione per interagire con l'API Django
def get_django_data():
    try:
        # Effettua una richiesta GET all'API Django
        import requests
        response = requests.get(f"{DJANGO_API_URL}/your-api-endpoint/")
        if response.status_code == 200:
            return response.json()  # Assicurati che l'API restituisca i dati in formato JSON
        else:
            st.error(f"Errore nell'accesso all'API Django: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Errore nella connessione all'API Django: {e}")
        return None

# Titolo dell'applicazione
st.title("Streamlit connesso a Postgres Gold e API Django")

# Carica i dati dal database Gold
st.subheader("Dati da Gold Database:")
data = get_data_from_gold_db()
if data is not None:
    st.write(data)

# Carica i dati dall'API Django
st.subheader("Dati dall'API Django:")
#django_data = get_django_data()
#if django_data is not None:
#    st.json(django_data)

