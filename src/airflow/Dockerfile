FROM apache/airflow:2.10.3

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openjdk-17-jdk \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER airflow
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
