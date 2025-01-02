FROM apache/airflow:2.10.3

USER root

# Installa eventuali dipendenze di sistema necessarie
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia la directory dei plugins
COPY plugins/ /opt/airflow/plugins/

# Copia le configurazioni
COPY config/ /opt/airflow/config/

USER airflow

# Se hai bisogno di installare dipendenze Python specifiche per i plugins,
# decommentare e aggiungere il file requirements
# COPY requirements.txt /opt/airflow/requirements.txt
# RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt