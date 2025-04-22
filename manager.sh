#!/bin/bash

CONFIG_DIR="src/airflow/config"
MERGE_ENV_SCRIPT="$CONFIG_DIR/merge-airflow-env.sh"
ENV_FILE="$CONFIG_DIR/.env"

COMPOSE_DIR="docker/dev"
COMPOSE_FILES="-f $COMPOSE_DIR/compose.base.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.databases.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.airflow.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.nginx.yml"

# Funzione per generare il file .env
generate_env() {
    echo "🔧 Generazione file .env da config..."
    bash "$MERGE_ENV_SCRIPT"

    if [ -f "$ENV_FILE" ]; then
        echo "📤 Esportazione variabili da $ENV_FILE"
        set -a
        source "$ENV_FILE"
        set +a
    else
        echo "⚠️  File .env non trovato in $ENV_FILE"
    fi
}

case $1 in
    "env")
        generate_env
        ;;
    "up")
        generate_env
        echo "🚀 Avvio dei container..."
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES up --build --remove-orphans "$2"
        else
            docker compose $COMPOSE_FILES up --build --remove-orphans 
        fi
        ;;
    "down")
        echo "🛑 Arresto dei container e rimozione dei volumi..."
        docker compose $COMPOSE_FILES down --volumes
        ;;
    "build")
        echo "🔨 Build dei container..."
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES build "$2"
        else
            docker compose $COMPOSE_FILES build
        fi
        ;;
    "logs")
        echo "📜 Log in tempo reale..."
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES logs -f "$2"
        else
            docker compose $COMPOSE_FILES logs -f
        fi
        ;;
    *)
        echo "Usage: ./manager.sh [env|up|down|build|logs] [service_name]"
        echo ""
        echo "Comandi disponibili:"
        echo "  env               # genera il file .env (senza avviare nulla)"
        echo "  up                # avvia tutti i container"
        echo "  up SERVICE        # avvia solo il container specificato"
        echo "  down              # ferma tutto e rimuove i volumi"
        echo "  build             # builda tutti i container"
        echo "  build SERVICE     # builda solo il container specificato"
        echo "  logs              # mostra i log di tutti i servizi"
        echo "  logs SERVICE      # mostra i log di un servizio specifico"
        ;;
esac
