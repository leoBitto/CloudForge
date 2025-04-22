#!/bin/bash

# Posizione dello script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# File di output
OUTPUT_FILE="$SCRIPT_DIR/.env"

# Inizializza o sovrascrive il file .env
> "$OUTPUT_FILE"

echo "📦 Unione file .conf nella directory: $SCRIPT_DIR"

# Scorre tutti i .conf nella directory corrente (nessuna sottodirectory)
for conf_file in "$SCRIPT_DIR"/*.conf; do
  if [[ -f "$conf_file" ]]; then
    echo "➕ Aggiungendo $conf_file"
    cat "$conf_file" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"  # newline tra i file
  fi
done

echo "✅ File .env generato: $OUTPUT_FILE"
