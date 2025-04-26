# /src/airflow/dockerfile
FROM apache/airflow:slim-3.0.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Crea le directory standard (solo come esempio, verranno sovrascritte dai volumi)
RUN mkdir -p /opt/airflow/dags /opt/airflow/plugins /opt/airflow/logs && \
    chown -R airflow: /opt/airflow


USER airflow

RUN pip install --upgrade pip setuptools wheel
# Aggiungi il requirements.txt
COPY ./src/airflow/requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
