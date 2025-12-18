# Installation & Schnellstart

## 📋 Voraussetzungen

- **Python:** 3.11 oder höher
- **uv:** UV Package Manager
- **Git:** Für Repository-Klonen (optional)

### UV installieren

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mit Homebrew (macOS)
brew install uv

# Installation prüfen
uv --version
```

### Python-Version prüfen

```bash
python3 --version
# Sollte ausgeben: Python 3.11.x oder höher
```

## 🚀 Installation

### Option 1: Aus dem Repository (Empfohlen für Entwicklung)

```bash
# 1. In das Projektverzeichnis wechseln
cd modul-4-agentic-coding/06-musterlösungen/aufgabe-1

# 2. Projekt initialisieren und alle Dependencies installieren
uv sync --all-extras

# 3. Installation testen
uv run task --version
```

### Option 2: Nur Runtime-Dependencies

```bash
# Ohne Development-Tools (pytest, black, etc.)
uv sync
```

### Option 3: Manuelle Installation

```bash
# Paket installieren
uv pip install -e .

# Mit Development-Dependencies
uv pip install -e ".[dev]"
```

## ✅ Installation verifizieren

### 1. CLI testen

```bash
# Hilfe anzeigen
uv run task --help

# Version anzeigen
uv run task --version
```

**Erwartete Ausgabe:**
```
Usage: task [OPTIONS] COMMAND [ARGS]...

  Task Manager - Verwalte deine Aufgaben effizient.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  add       Fügt eine neue Aufgabe hinzu.
  complete  Markiert eine Aufgabe als erledigt.
  delete    Löscht eine Aufgabe.
  list      Listet alle Aufgaben auf.
  stats     Zeigt Statistiken über alle Aufgaben.
```

### 2. Tests ausführen (nur mit dev-Dependencies)

```bash
# Alle Tests
uv run pytest

# Mit Coverage
uv run pytest --cov=task_manager

# Verbose-Modus
uv run pytest -v
```

**Erwartete Ausgabe:**
```
============================== 39 passed in 0.17s ===============================
Coverage: 89%
```

### 3. Code-Qualität prüfen (nur mit dev-Dependencies)

```bash
# Formatierung prüfen
uv run black --check task_manager tests

# Linting
uv run flake8 task_manager

# Type Checking
uv run mypy task_manager
```

## 🎯 Schnellstart

### Erste Schritte

```bash
# 1. Task erstellen
uv run task add "Meine erste Aufgabe" --priority high

# 2. Tasks auflisten
uv run task list

# 3. Task erledigen
uv run task complete 1

# 4. Statistiken anzeigen
uv run task stats
```

### Demo ausführen

```bash
# Demo-Skript ausführen (zeigt alle Features)
chmod +x demo.sh
./demo.sh
```

### Mit Makefile (empfohlen)

```bash
# Alle verfügbaren Commands anzeigen
make help

# Tests ausführen
make test

# Tests mit Coverage
make test-cov

# Code formatieren
make format

# Alle Checks ausführen
make all

# Demo ausführen
make demo
```

## 📁 Datenverzeichnis

Nach der ersten Verwendung wird folgendes Verzeichnis erstellt:

```
~/.task_manager/
├── tasks.json          # Task-Daten
└── task_manager.log    # Log-Datei
```

### Daten zurücksetzen

```bash
# Alle Tasks löschen
rm ~/.task_manager/tasks.json

# Logs löschen
rm ~/.task_manager/task_manager.log

# Komplettes Verzeichnis löschen
rm -rf ~/.task_manager/
```

## 🔧 Troubleshooting

### Problem: `command not found: task`

**Lösung:** UV verwenden
```bash
uv run task --help
```

### Problem: `ModuleNotFoundError: No module named 'click'`

**Lösung:** Dependencies installieren
```bash
uv sync --all-extras
```

### Problem: Tests schlagen fehl

**Lösung 1:** Dependencies neu installieren
```bash
rm -rf .venv
uv sync --all-extras
```

**Lösung 2:** Cache löschen
```bash
rm -rf .pytest_cache
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -rf {} +
uv cache clean
```

### Problem: Python-Version zu alt

**Lösung:** Python 3.11+ installieren

**macOS (mit Homebrew):**
```bash
brew install python@3.11
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.11
```

**Windows:**
- Download von [python.org](https://www.python.org/downloads/)

## 🎓 Nächste Schritte

1. **Dokumentation lesen:** [README.md](./README.md)
2. **Code verstehen:** [LÖSUNGSHINWEISE.md](./LÖSUNGSHINWEISE.md)
3. **Struktur erkunden:** [PROJEKTSTRUKTUR.md](./PROJEKTSTRUKTUR.md)
4. **Beitragen:** [CONTRIBUTING.md](./CONTRIBUTING.md)

## 💡 Tipps

- **UV verwenden:** Alle Commands mit `uv run` ausführen
- **Tests:** Regelmässig ausführen während der Entwicklung
- **Logs:** Bei Problemen in `~/.task_manager/task_manager.log` schauen
- **Demo:** Zeigt alle Features in Aktion
- **UV Cache:** Bei Problemen `uv cache clean` ausführen

---

**Zurück zu:** [README](./README.md)

