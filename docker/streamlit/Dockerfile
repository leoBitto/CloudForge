FROM python:3.10-slim

WORKDIR /app

COPY ../src/streamlit/ .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["streamlit", "run", "app.py"]