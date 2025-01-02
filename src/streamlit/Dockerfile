FROM python:3.10-slim

WORKDIR /src

COPY ./requirements.txt /src/
#COPY ./app /src/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /src/requirements.txt


CMD ["streamlit", "run", "app.py"]