FROM python:3.10-slim

WORKDIR /home/app

# Copia tutti i file necessari
COPY . .

# Installa dipendenze
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements-test.txt

# Imposta PYTHONPATH in modo esplicito
ENV PYTHONPATH=/home/app/src/django:$PYTHONPATH

# Comandi di test
CMD ["pytest", "/home/app/tests", "--disable-warnings", "-v"]