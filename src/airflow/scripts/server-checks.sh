#!/usr/bin/env bash

set -euo pipefail

echo "🔍 Avvio controlli pre-Airflow..."

# Check risorse minime disponibili
one_meg=1048576
mem_available=$(( $(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE) / one_meg ))
cpus_available=$(grep -cE 'cpu[0-9]+' /proc/stat)
disk_available=$(df / | tail -1 | awk '{print $4}')

warning_resources="false"

if (( mem_available < 3000 )); then
  echo -e "\033[1;33m⚠️  RAM insufficiente: richiesti almeno 4GB, trovati $((mem_available)) MB\e[0m"
  warning_resources="true"
fi

if (( cpus_available < 2 )); then
  echo -e "\033[1;33m⚠️  CPU insufficienti: richieste almeno 2, trovate ${cpus_available}\e[0m"
  warning_resources="true"
fi

if (( disk_available < one_meg * 10 )); then
  echo -e "\033[1;33m⚠️  Spazio disco insufficiente: richiesti almeno 10GB, trovati $((disk_available * 1024)) Bytes\e[0m"
  warning_resources="true"
fi

if [[ $warning_resources == "true" ]]; then
  echo -e "\033[1;33m⚠️  ATTENZIONE: Risorse insufficienti per avviare Airflow in modo stabile\e[0m"
fi


