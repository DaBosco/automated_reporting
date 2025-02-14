#!/bin/bash

# Trova la directory dello script corrente
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

# Esegui gli script Python con percorsi relativi
python3 "$BASE_DIR/scripts/generate_report.py"
python3 "$BASE_DIR/scripts/send_email.py"

