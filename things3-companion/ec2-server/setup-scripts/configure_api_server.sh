#!/bin/bash
set -e
REPO_DIR="$HOME/evelion-apps-things-api"
if [ ! -d "$REPO_DIR" ]; then
    git clone https://github.com/evelion-apps/things-api.git "$REPO_DIR"
fi
cd "$REPO_DIR"
cp .env.local.example .env.local
# Update SYNC_DB_* variables as needed
bin/install
