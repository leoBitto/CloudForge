#!/bin/bash
COMPOSEFILE="./docker/docker-compose.dev.yml"

# Questa funzione elimina le immagini precedenti e avvia i container
build_and_start_containers() {
    echo "Eliminazione dei container e volumi esistenti..."
    sudo docker compose -f $COMPOSEFILE down -v --remove-orphans

    echo "Creazione e avvio dei container Docker..."
    sudo docker compose -f $COMPOSEFILE up --build || echo "Non è stato possibile costruire le immagini"
    echo "Immagini create"

}

# Questa funzione avvia solo i container Docker
start_containers() {
    echo "Avvio dei container Docker in background..."
    sudo docker compose -f $COMPOSEFILE up -d
    echo "Container avviati"
}

# Questa funzione ferma i container Docker
stop_containers() {
    echo "Arresto di tutti i container Docker..."
    sudo docker compose -f $COMPOSEFILE down
    echo "Server fermato"
}

# Questa funzione elimina tutti i container e i volumi
destroy_containers() {
    echo "Eliminazione di tutti i container e volumi..."
    sudo docker compose -f $COMPOSEFILE down -v --remove-orphans
    echo "Container e volumi eliminati"
}

# Controlla gli argomenti passati allo script
case "$1" in
    build)
        build_and_start_containers
        ;;
    start)
        start_containers
        ;;
    stop)
        stop_containers
        ;;
    destroy)
        destroy_containers
        ;;
    *)
        echo "Utilizzo: $0 {build|start|stop|destroy}"
        exit 1
        ;;
esac
