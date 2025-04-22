FROM apache/airflow:2.10.3

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-17-jdk \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow

# Rimuovi il file airflow.cfg predefinito
RUN rm -f /opt/airflow/airflow.cfg

RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
