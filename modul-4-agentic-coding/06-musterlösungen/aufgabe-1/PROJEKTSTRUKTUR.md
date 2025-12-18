# Projektstruktur - Task Manager CLI

## 📁 Übersicht

```
task-manager-cli/
├── task_manager/              # Hauptpaket
│   ├── __init__.py           # Package-Initialisierung
│   ├── cli.py                # CLI-Commands (Click)
│   ├── models.py             # Datenmodelle
│   └── storage.py            # Storage-Layer
│
├── tests/                     # Test-Suite
│   ├── __init__.py
│   ├── test_cli.py           # CLI-Tests
│   ├── test_models.py        # Model-Tests
│   └── test_storage.py       # Storage-Tests
│
├── .github/                   # GitHub-Konfiguration
│   └── workflows/
│       └── test.yml          # CI/CD Pipeline
│
├── .gitignore                # Git-Ignore-Regeln
├── .flake8                   # Flake8-Konfiguration
├── CHANGELOG.md              # Versionshistorie
├── CONTRIBUTING.md           # Contribution-Guidelines
├── LICENSE                   # MIT-Lizenz
├── Makefile                  # Build-Automatisierung
├── README.md                 # Hauptdokumentation
├── LÖSUNGSHINWEISE.md        # Detaillierte Erklärungen
├── PROJEKTSTRUKTUR.md        # Diese Datei
├── UV-GUIDE.md               # UV Package Manager Guide
├── UV-MIGRATION.md           # UV Migrations-Dokumentation
├── demo.sh                   # Demo-Skript
├── pyproject.toml            # Projekt-Konfiguration (UV nutzt diese)
└── uv.lock                   # UV Lock-File (Dependencies)
```

## 📦 Hauptpaket (`task_manager/`)

### `__init__.py`
- Package-Initialisierung
- Version und Autor-Informationen
- Exports für öffentliche API

### `models.py`
**Zweck:** Datenmodelle und Business-Logik

**Klassen:**
- `Priority(Enum)` - Task-Prioritäten (low, medium, high)
- `Status(Enum)` - Task-Status (open, done)
- `Task(dataclass)` - Hauptmodell für Tasks

**Methoden:**
- `to_dict()` - Serialisierung zu Dictionary
- `from_dict()` - Deserialisierung von Dictionary
- `complete()` - Task als erledigt markieren
- `__str__()` - String-Repräsentation

**Design-Entscheidungen:**
- Dataclass für weniger Boilerplate
- Enums für Type-Safety
- Immutable wo möglich

### `storage.py`
**Zweck:** Persistenz-Layer für Tasks

**Klasse:**
- `TaskStorage` - Repository für Task-Verwaltung

**Methoden:**
- `load_tasks()` - Alle Tasks laden
- `save_tasks()` - Alle Tasks speichern
- `add_task()` - Task hinzufügen
- `get_task()` - Task abrufen
- `update_task()` - Task aktualisieren
- `delete_task()` - Task löschen
- `get_next_id()` - Nächste freie ID
- `filter_tasks()` - Tasks filtern

**Design-Entscheidungen:**
- Repository Pattern
- JSON für Einfachheit
- Automatische Verzeichnis-Erstellung
- Fehlerbehandlung für ungültiges JSON

### `cli.py`
**Zweck:** Command-Line Interface

**Commands:**
- `add` - Task hinzufügen
- `list` - Tasks auflisten
- `complete` - Task erledigen
- `delete` - Task löschen
- `stats` - Statistiken anzeigen

**Features:**
- Click-Framework
- Farbige Ausgabe
- Fehlerbehandlung
- Logging
- Help-Texte

**Design-Entscheidungen:**
- Deklarativer Stil mit Click
- Konsistente Fehlerbehandlung
- Benutzerfreundliche Ausgabe

## 🧪 Tests (`tests/`)

### `test_models.py`
**Zweck:** Tests für Datenmodelle

**Test-Klassen:**
- `TestTask` - Task-Funktionalität
- `TestPriority` - Priority-Enum
- `TestStatus` - Status-Enum

**Abdeckung:**
- Task-Erstellung
- Serialisierung/Deserialisierung
- Status-Änderungen
- String-Repräsentation

### `test_storage.py`
**Zweck:** Tests für Storage-Layer

**Test-Klasse:**
- `TestTaskStorage` - Storage-Funktionalität

**Abdeckung:**
- CRUD-Operationen
- Fehlerbehandlung
- Persistenz
- Filterung

**Fixtures:**
- `temp_storage` - Temporärer Storage für Tests

### `test_cli.py`
**Zweck:** Tests für CLI-Commands

**Test-Klassen:**
- `TestCLI` - Allgemeine CLI-Tests
- `TestAddCommand` - Add-Command
- `TestListCommand` - List-Command
- `TestCompleteCommand` - Complete-Command
- `TestDeleteCommand` - Delete-Command
- `TestStatsCommand` - Stats-Command

**Fixtures:**
- `runner` - Click CLI Runner
- `temp_storage_path` - Temporärer Storage-Pfad

## ⚙️ Konfiguration

### `pyproject.toml`
**Zweck:** Zentrale Projekt-Konfiguration (UV nutzt diese)

**Sektionen:**
- `[build-system]` - Build-Konfiguration
- `[project]` - Projekt-Metadaten und Dependencies
- `[project.optional-dependencies]` - Dev-Dependencies
- `[project.scripts]` - CLI Entry Points
- `[tool.black]` - Black-Konfiguration
- `[tool.pytest.ini_options]` - Pytest-Konfiguration
- `[tool.mypy]` - Mypy-Konfiguration
- `[tool.coverage]` - Coverage-Konfiguration

### `uv.lock`
**Zweck:** Lock-File für reproduzierbare Builds

**Features:**
- Exakte Versionen aller Dependencies
- Transitive Dependencies
- Plattform-spezifische Informationen
- Automatisch von UV generiert

### `.flake8`
**Zweck:** Linting-Konfiguration

**Einstellungen:**
- Max Line Length: 100
- Excludes: Build-Verzeichnisse
- Ignores: Black-Kompatibilität

## 🔄 CI/CD (`.github/workflows/`)

### `test.yml`
**Zweck:** Automatisierte Tests und Checks (mit UV)

**Jobs:**
1. **test** - Tests ausführen
   - Matrix: Ubuntu, macOS, Windows
   - Python: 3.11, 3.12
   - UV Installation: `astral-sh/setup-uv@v5`
   - Steps: `uv sync`, Lint, Format, Type-Check, Tests

2. **build** - Package bauen
   - UV Build: `uv build`
   - Build-Artefakte erstellen

## 📚 Dokumentation

### `README.md`
- Projekt-Übersicht
- Installation
- Verwendung
- Features
- Bewertungskriterien

### `LÖSUNGSHINWEISE.md`
- Detaillierte Erklärungen
- Design-Entscheidungen
- Best Practices
- Lernpunkte

### `CONTRIBUTING.md`
- Contribution-Guidelines
- Code-Standards
- PR-Prozess
- UV-basierter Workflow

### `UV-GUIDE.md`
- Umfassender UV Package Manager Guide
- Installation und Verwendung
- Befehlsreferenz
- Best Practices
- Troubleshooting

### `UV-MIGRATION.md`
- Migrations-Dokumentation von pip zu UV
- Schritt-für-Schritt Anleitung
- Befehlsvergleiche
- Häufige Fragen
- Code of Conduct

### `CHANGELOG.md`
- Versionshistorie
- Änderungen
- Geplante Features

## 🛠️ Hilfsskripte

### `Makefile`
**Zweck:** Automatisierung häufiger Tasks

**Targets:**
- `install` - Paket installieren
- `test` - Tests ausführen
- `lint` - Linting
- `format` - Code formatieren
- `clean` - Aufräumen

### `demo.sh`
**Zweck:** Demo aller Features

**Ablauf:**
1. Tasks erstellen
2. Tasks auflisten
3. Tasks erledigen
4. Statistiken anzeigen
5. Tasks löschen

---

**Zurück zu:** [README](./README.md)

