#!/bin/bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"
PROJECT_DIR="/home/weidademiaoxiao/music-appreciation-api-coursework"
WHEELHOUSE_DIR="$PROJECT_DIR/wheelhouse"
REQUIREMENTS_FILE="$PROJECT_DIR/requirements-deploy.txt"
PIP_LOG="/home/weidademiaoxiao/music_appreciation_pip_install.log"

cd "$PROJECT_DIR"
python3.10 -m pip install --user --disable-pip-version-check --no-index --find-links "$WHEELHOUSE_DIR" -r "$REQUIREMENTS_FILE" > "$PIP_LOG" 2>&1
exec python3.10 -m uvicorn --app-dir "$PROJECT_DIR" --uds "${DOMAIN_SOCKET}" app.main:app
