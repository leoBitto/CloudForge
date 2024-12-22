FROM python:3.10-slim

WORKDIR /app

COPY ./src/streamlit/ /app/

RUN pip install --upgrade pip
#COPY ./src/streamlit/requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt


CMD ["streamlit", "run", "app.py"]