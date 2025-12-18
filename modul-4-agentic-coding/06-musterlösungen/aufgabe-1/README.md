# Task Manager CLI

Ein vollständiges Command-Line Tool für effiziente Task-Verwaltung, entwickelt als Musterlösung für die Aufgabe 1 des Moduls "Agentic Coding".

[![Tests](https://github.com/talent-factory/task-manager-cli/workflows/Tests/badge.svg)](https://github.com/talent-factory/task-manager-cli/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🎯 Features

- ✅ **Task-Verwaltung**: Erstellen, Auflisten, Erledigen und Löschen von Tasks
- 🎨 **Prioritäten**: Drei Prioritätsstufen (low, medium, high)
- 📊 **Statistiken**: Übersicht über alle Tasks und deren Status
- 💾 **Persistenz**: Automatisches Speichern in JSON-Datei
- 🎨 **Farbige Ausgabe**: Übersichtliche CLI mit Icons und Farben
- 📝 **Logging**: Vollständiges Logging aller Aktionen
- ✅ **Tests**: Umfassende Unit-Tests mit pytest
- 🔄 **CI/CD**: Automatisierte Tests mit GitHub Actions
- ⚡ **UV:** Moderner Package Manager für schnelle Installation

## 📦 Installation

### Voraussetzungen

- Python 3.11 oder höher
- uv (UV Package Manager)

### UV installieren

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mit Homebrew (macOS)
brew install uv
```

### Installation aus dem Repository

```bash
# Repository klonen
git clone https://github.com/talent-factory/task-manager-cli.git
cd task-manager-cli

# Projekt initialisieren und Dependencies installieren
uv sync

# Paket installieren
uv pip install -e .
```

### Installation für Entwicklung

```bash
# Mit Development-Dependencies installieren
uv sync --all-extras
```

## 🚀 Verwendung

### Tasks erstellen

```bash
# Task mit Standard-Priorität (medium)
task add "Code reviewen"

# Task mit hoher Priorität
task add "Bug fixen" --priority high

# Task mit niedriger Priorität
task add "Dokumentation aktualisieren" -p low
```

### Tasks auflisten

```bash
# Alle Tasks anzeigen
task list

# Nur offene Tasks
task list --status open

# Nur erledigte Tasks
task list --status done
```

### Tasks erledigen

```bash
# Task als erledigt markieren
task complete 1
```

### Tasks löschen

```bash
# Task löschen (mit Bestätigung)
task delete 1
```

### Statistiken anzeigen

```bash
# Übersicht über alle Tasks
task stats
```

## 📁 Projektstruktur

```
task-manager-cli/
├── task_manager/           # Hauptpaket
│   ├── __init__.py        # Package-Initialisierung
│   ├── cli.py             # CLI-Commands (Click)
│   ├── models.py          # Datenmodelle (Task, Priority, Status)
│   └── storage.py         # JSON-Storage-Layer
├── tests/                  # Test-Suite
│   ├── __init__.py
│   ├── test_cli.py        # CLI-Tests
│   ├── test_models.py     # Model-Tests
│   └── test_storage.py    # Storage-Tests
├── .github/
│   └── workflows/
│       └── test.yml       # GitHub Actions CI/CD
├── .gitignore
├── README.md
├── requirements.txt       # Dependencies
├── setup.py              # Setup-Konfiguration
└── pyproject.toml        # Projekt-Konfiguration
```

## 🧪 Tests ausführen

```bash
# Alle Tests ausführen
uv run pytest

# Mit Coverage-Report
uv run pytest --cov=task_manager --cov-report=html

# Spezifische Test-Datei
uv run pytest tests/test_cli.py

# Einzelnen Test ausführen
uv run pytest tests/test_models.py::TestTask::test_task_creation
```

## 🔧 Entwicklung

### Code-Qualität

```bash
# Code formatieren mit black
uv run black task_manager tests

# Linting mit flake8
uv run flake8 task_manager

# Type-Checking mit mypy
uv run mypy task_manager
```

### Logging

Logs werden gespeichert in: `~/.task_manager/task_manager.log`

### Storage

Tasks werden gespeichert in: `~/.task_manager/tasks.json`

### UV Package Manager

Dieses Projekt verwendet UV statt pip. Siehe [UV-GUIDE.md](./UV-GUIDE.md) für Details.

## 📊 Bewertungskriterien

| Kriterium | Punkte | Erfüllt |
|-----------|--------|---------|
| **Funktionalität** | 10 | ✅ |
| - Mehrere Commands (5) | | ✅ |
| - Argument-Parsing (click) | | ✅ |
| - Konfigurationsdatei (JSON) | | ✅ |
| - Fehlerbehandlung | | ✅ |
| - Logging | | ✅ |
| **Code-Qualität** | 8 | ✅ |
| - Type Hints | | ✅ |
| - Docstrings | | ✅ |
| - Clean Code | | ✅ |
| **Tests** | 7 | ✅ |
| - Unit Tests (pytest) | | ✅ |
| - Test Coverage > 80% | | ✅ |
| **Dokumentation** | 5 | ✅ |
| - README.md | | ✅ |
| - Code-Kommentare | | ✅ |
| **CI/CD** | 5 | ✅ |
| - GitHub Actions | | ✅ |
| - Automatische Tests | | ✅ |
| **Gesamt** | **35** | **✅** |

## 🎓 Lernziele

Diese Musterlösung demonstriert:

1. **CLI-Entwicklung**: Professionelle CLI-Anwendung mit Click
2. **Datenmodellierung**: Verwendung von Dataclasses und Enums
3. **Persistenz**: JSON-basierte Datenspeicherung
4. **Testing**: Umfassende Test-Suite mit pytest
5. **CI/CD**: Automatisierte Tests und Builds
6. **Code-Qualität**: Type Hints, Docstrings, Formatierung
7. **Fehlerbehandlung**: Robuste Error-Handling-Strategien
8. **Logging**: Strukturiertes Logging für Debugging

## 📝 Lizenz

MIT License - siehe LICENSE-Datei für Details.

## 👥 Autor

Talent Factory - Python Training

---

**Zurück zu:** [Aufgabe 1](../../03-nachbearbeitung/aufgabe-1-cli-tool.md)

