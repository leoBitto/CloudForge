#!/bin/bash

COMPOSE_DIR="docker/dev"
COMPOSE_FILES="-f $COMPOSE_DIR/compose.base.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.databases.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.django.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.airflow.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.streamlit.yml"
#COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.monitoring.yml"
COMPOSE_FILES="$COMPOSE_FILES -f $COMPOSE_DIR/compose.nginx.yml"

case $1 in
    "up")
        # Se viene specificato un servizio, avvia solo quello
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES up --build --remove-orphans $2
        else
            docker compose $COMPOSE_FILES up --build --remove-orphans 
        fi
        ;;
    "down")
        docker compose $COMPOSE_FILES down
        ;;
    "build")
        # Se viene specificato un servizio, rebuilda solo quello
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES build $2
        else
            docker compose $COMPOSE_FILES build
        fi
        ;;
    "logs")
        if [ -n "$2" ]; then
            docker compose $COMPOSE_FILES logs -f $2
        else
            docker compose $COMPOSE_FILES logs -f
        fi
        ;;
    *)
        echo "Usage: ./manager.sh [up|down|build|logs] [service_name]"
        echo "Examples:"
        echo "  ./manager.sh up              # avvia tutti i servizi"
        echo "  ./manager.sh up django-app   # avvia solo django"
        echo "  ./manager.sh build           # rebuilda tutti i servizi"
        echo "  ./manager.sh build streamlit # rebuilda solo streamlit"
        echo "  ./manager.sh logs django-app # mostra i log di django"
        exit 1
        ;;
esac