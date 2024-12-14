# Usa una base Python ufficiale
FROM python:3.10-slim

# Imposta la cartella di lavoro
WORKDIR /home/app

# Copia il requirements.txt nella cartella di lavoro
COPY ./requirements.txt .

# Installa le dipendenze del progetto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice sorgente per i test (a seconda della tua struttura)
COPY ./src/ .

# Copia la cartella dei test
COPY ./tests/ ./tests/

# Aggiungi un comando per eseguire i test (puoi personalizzarlo come vuoi)
CMD ["pytest", "--maxfail=5", "--disable-warnings", "--maxfail=1"]
