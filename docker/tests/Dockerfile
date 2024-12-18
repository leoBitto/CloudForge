FROM python:3.10-slim

WORKDIR /home/app

# Copia tutti i file necessari
COPY . .

# Installa dipendenze
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Imposta PYTHONPATH in modo esplicito
ENV PYTHONPATH=/home/app/src/django:$PYTHONPATH

# Debug steps
RUN pwd
RUN ls -R ./tests
RUN python -c "import sys; print('\n'.join(sys.path))"

# Comandi di test
CMD ["pytest", "/home/app/tests", "--disable-warnings", "-v"]