#!/bin/bash

# Configurazione percorsi
COMPOSE_DIR="docker/dev"
COMPOSE_FILES="-f $COMPOSE_DIR/compose.base.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.databases.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.airflow.yml"
# COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.nginx.yml" # Non usato ora

# Percorsi locali da verificare/creare
AIRFLOW_DIR="src/airflow"
DIRECTORIES=("dags" "logs" "plugins")

# Funzione per preparare l'ambiente
prepare_directories() {
    echo "🔧 Verifica delle directory richieste..."
    for dir in "${DIRECTORIES[@]}"; do
        PATH_TO_CREATE="$AIRFLOW_DIR/$dir"
        if [ ! -d "$PATH_TO_CREATE" ]; then
            echo "➔ Creazione cartella mancante: $PATH_TO_CREATE"
            mkdir -p "$PATH_TO_CREATE"
            chmod 775 "$PATH_TO_CREATE"
        fi
    done
}

# Funzioni principali
up() {
    prepare_directories
    echo "🚀 Avvio dei container..."
    if [ -n "$1" ]; then
        docker compose $COMPOSE_FILES up --build --remove-orphans "$1"
    else
        docker compose $COMPOSE_FILES up --build --remove-orphans
    fi
}

down() {
    echo "🛑 Arresto dei container e rimozione dei volumi..."
    docker compose $COMPOSE_FILES down --volumes
}

build() {
    prepare_directories
    echo "🔨 Build dei container..."
    if [ -n "$1" ]; then
        docker compose $COMPOSE_FILES build "$1"
    else
        docker compose $COMPOSE_FILES build
    fi
}

logs() {
    echo "📜 Log in tempo reale..."
    if [ -n "$1" ]; then
        docker compose $COMPOSE_FILES logs -f "$1"
    else
        docker compose $COMPOSE_FILES logs -f
    fi
}

# Comandi
case $1 in
    "up")        up "$2" ;;
    "down")      down ;;
    "build")     build "$2" ;;
    "logs")      logs "$2" ;;
    *)
        echo "Usage: ./manager.sh [up|down|build|logs] [service_name]"
        echo ""
        echo "Comandi disponibili:"
        echo "  up                # avvia tutti i container"
        echo "  up SERVICE        # avvia solo il container specificato"
        echo "  down              # ferma tutto e rimuove i volumi"
        echo "  build             # builda tutti i container"
        echo "  build SERVICE     # builda solo il container specificato"
        echo "  logs              # mostra i log di tutti i servizi"
        echo "  logs SERVICE      # mostra i log di un servizio specificato"
        ;;
esac
