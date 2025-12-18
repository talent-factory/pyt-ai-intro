# UV Package Manager Guide

Dieses Projekt verwendet **UV** als Package Manager anstelle von pip. UV ist ein moderner, schneller Python Package Manager von Astral.

## 🚀 Warum UV?

- ⚡ **Schneller:** Bis zu 10-100x schneller als pip
- 🔒 **Zuverlässig:** Deterministisches Dependency Resolution
- 🎯 **Einfach:** Weniger Befehle, mehr Automatisierung
- 🔄 **Modern:** Unterstützt moderne Python-Features
- 📦 **Integriert:** Kombiniert venv, pip, und mehr

## 📦 Installation

### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Mit Homebrew (macOS)

```bash
brew install uv
```

### Installation prüfen

```bash
uv --version
```

## 🎯 Grundlegende Befehle

### Projekt initialisieren

```bash
# Dependencies aus pyproject.toml installieren
uv sync

# Mit allen optionalen Dependencies (dev, test, etc.)
uv sync --all-extras
```

### Pakete installieren

```bash
# Einzelnes Paket installieren
uv pip install click

# Paket mit Version
uv pip install "click>=8.1.7"

# Aus requirements.txt
uv pip install -r requirements.txt

# Editable Installation (Development)
uv pip install -e .
uv pip install -e ".[dev]"
```

### Befehle ausführen

```bash
# Python-Skript ausführen
uv run python script.py

# Installiertes Command ausführen
uv run task --help
uv run pytest
uv run black .

# Mit Argumenten
uv run task add "Neue Aufgabe" --priority high
```

### Pakete verwalten

```bash
# Installierte Pakete auflisten
uv pip list

# Paket deinstallieren
uv pip uninstall click

# Alle Pakete aktualisieren
uv sync --upgrade
```

### Cache verwalten

```bash
# Cache anzeigen
uv cache dir

# Cache löschen
uv cache clean
```

## 🔧 Projekt-spezifische Befehle

### Development Setup

```bash
# Projekt klonen und einrichten
git clone <repository>
cd task-manager-cli

# Dependencies installieren
uv sync --all-extras
```

### Tests

```bash
# Alle Tests
uv run pytest

# Mit Coverage
uv run pytest --cov=task_manager

# Spezifische Tests
uv run pytest tests/test_cli.py

# Verbose
uv run pytest -v
```

### Code-Qualität

```bash
# Formatierung
uv run black task_manager tests

# Formatierung prüfen
uv run black --check task_manager tests

# Linting
uv run flake8 task_manager

# Type Checking
uv run mypy task_manager
```

### CLI verwenden

```bash
# Hilfe
uv run task --help

# Task hinzufügen
uv run task add "Meine Aufgabe" --priority high

# Tasks auflisten
uv run task list

# Task erledigen
uv run task complete 1

# Statistiken
uv run task stats
```

### Build

```bash
# Package bauen
uv build

# Wheel und Source Distribution
uv build --wheel
uv build --sdist
```

## 📚 UV vs. pip Vergleich

| Aufgabe | pip | UV |
|---------|-----|-----|
| Venv erstellen | `python -m venv venv` | Automatisch |
| Venv aktivieren | `source venv/bin/activate` | Nicht nötig |
| Paket installieren | `pip install click` | `uv pip install click` |
| Requirements installieren | `pip install -r requirements.txt` | `uv sync` |
| Editable install | `pip install -e .` | `uv pip install -e .` |
| Command ausführen | `pytest` | `uv run pytest` |
| Cache löschen | `pip cache purge` | `uv cache clean` |

## 💡 Best Practices

### 1. Verwende `uv sync`

```bash
# Statt pip install -r requirements.txt
uv sync --all-extras
```

**Vorteile:**
- Liest automatisch `pyproject.toml`
- Installiert alle Dependencies
- Erstellt Lock-File für Reproduzierbarkeit

### 2. Verwende `uv run`

```bash
# Statt venv aktivieren und dann ausführen
uv run pytest
uv run task --help
```

**Vorteile:**
- Keine manuelle venv-Aktivierung
- Automatische Umgebungsverwaltung
- Funktioniert überall gleich

### 3. Lock-File committen

```bash
# uv.lock sollte im Git sein
git add uv.lock
git commit -m "Update dependencies"
```

**Vorteile:**
- Reproduzierbare Builds
- Gleiche Versionen im Team
- CI/CD-Konsistenz

### 4. Cache nutzen

```bash
# UV cached automatisch
# Bei Problemen:
uv cache clean
```

## 🔍 Troubleshooting

### Problem: `command not found: uv`

**Lösung:** UV installieren
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Problem: Dependencies nicht gefunden

**Lösung:** Sync ausführen
```bash
uv sync --all-extras
```

### Problem: Alte Versionen im Cache

**Lösung:** Cache löschen
```bash
uv cache clean
uv sync --all-extras
```

### Problem: `uv run` findet Command nicht

**Lösung:** Prüfen ob installiert
```bash
uv pip list | grep task-manager
# Falls nicht:
uv pip install -e .
```

## 📖 Weitere Ressourcen

- **Offizielle Dokumentation:** https://docs.astral.sh/uv/
- **GitHub:** https://github.com/astral-sh/uv
- **Blog:** https://astral.sh/blog

## 🎓 Für Studierende

UV ist der moderne Standard für Python Package Management:

1. **Schneller:** Spart Zeit bei Installation
2. **Einfacher:** Weniger Befehle zu merken
3. **Zuverlässiger:** Konsistente Umgebungen
4. **Zukunftssicher:** Aktiv entwickelt

**Empfehlung:** Verwende UV für alle Python-Projekte!

---

**Zurück zu:** [README](./README.md)

