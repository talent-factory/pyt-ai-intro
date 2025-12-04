#!/bin/bash
# Git-Commit-System - Shell-Wrapper
# Verwendung: ./commit.sh [Optionen]

# Skript-Verzeichnis ermitteln
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Python-Skript ausführen
python3 "$SCRIPT_DIR/commit/commit.py" "$@"
