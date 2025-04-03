FROM apache/airflow:2.10.3

USER root

# Installa dipendenze di sistema necessarie (compreso Java per Spark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-11-jdk \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Imposta la variabile d'ambiente per Java (necessaria per Spark)
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow

# Copia il file requirements.txt ed installa i pacchetti Python
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
