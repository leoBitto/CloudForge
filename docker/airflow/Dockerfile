FROM apache/airflow:latest

# Install JDK
USER root
RUN apt update \
  && apt install -y --no-install-recommends \
  default-jdk \
  && apt autoremove -yqq --purge \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN pip install apache-airflow-providers-docker
COPY requirements.txt .
RUN pip install -r requirements.txt