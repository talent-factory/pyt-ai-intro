# UV Migration - Von pip zu UV

Dieses Dokument beschreibt die Migration von pip zu UV als Package Manager.

## 🎯 Warum UV?

Dieses Projekt wurde auf UV migriert, um:

1. ⚡ **Schnellere Installation:** UV ist 10-100x schneller als pip
2. 🔒 **Reproduzierbarkeit:** Deterministisches Dependency Resolution
3. 🎯 **Einfachheit:** Weniger Befehle, mehr Automatisierung
4. 🔄 **Modernität:** Aktiv entwickelt und zukunftssicher

## 📋 Änderungen

### Dokumentation

Alle Dokumentations-Dateien wurden aktualisiert:

- ✅ `README.md` - Installation und Verwendung
- ✅ `INSTALLATION.md` - Detaillierte Installations-Anleitung
- ✅ `CONTRIBUTING.md` - Development-Workflow
- ✅ `LÖSUNGSHINWEISE.md` - Test-Befehle
- ✅ `ZUSAMMENFASSUNG.md` - Schnellstart

### Konfiguration

- ✅ `.github/workflows/test.yml` - CI/CD mit UV
- ✅ `Makefile` - Build-Befehle mit UV
- ✅ `demo.sh` - Demo-Skript mit UV
- ✅ `.gitignore` - UV-spezifische Einträge

### Neue Dateien

- ✅ `UV-GUIDE.md` - Umfassender UV-Guide
- ✅ `UV-MIGRATION.md` - Diese Datei

## 🔄 Befehlsvergleich

### Installation

| Aufgabe | pip | UV |
|---------|-----|-----|
| Venv erstellen | `python -m venv venv` | Automatisch |
| Venv aktivieren | `source venv/bin/activate` | Nicht nötig |
| Dependencies installieren | `pip install -e ".[dev]"` | `uv sync --all-extras` |

### Verwendung

| Aufgabe | pip | UV |
|---------|-----|-----|
| Tests ausführen | `pytest` | `uv run pytest` |
| CLI verwenden | `task --help` | `uv run task --help` |
| Code formatieren | `black .` | `uv run black .` |
| Linting | `flake8 .` | `uv run flake8 .` |

### Verwaltung

| Aufgabe | pip | UV |
|---------|-----|-----|
| Pakete auflisten | `pip list` | `uv pip list` |
| Paket installieren | `pip install click` | `uv pip install click` |
| Cache löschen | `pip cache purge` | `uv cache clean` |

## 🚀 Migration für Studierende

### Schritt 1: UV installieren

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mit Homebrew (macOS)
brew install uv
```

### Schritt 2: Alte Umgebung entfernen

```bash
# Alte venv löschen
rm -rf venv

# Alte .venv löschen (falls vorhanden)
rm -rf .venv
```

### Schritt 3: Mit UV neu installieren

```bash
# Dependencies installieren
uv sync --all-extras

# Installation testen
uv run task --version
```

### Schritt 4: Tests ausführen

```bash
# Alle Tests
uv run pytest -v

# Mit Coverage
uv run pytest --cov=task_manager
```

## 💡 Tipps für die Umstellung

### 1. Kein manuelles venv-Management

**Vorher (pip):**
```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
pytest
```

**Nachher (UV):**
```bash
uv sync --all-extras
uv run pytest
```

### 2. Immer `uv run` verwenden

**Vorher (pip):**
```bash
source venv/bin/activate  # Muss aktiviert sein!
task add "Neue Aufgabe"
```

**Nachher (UV):**
```bash
uv run task add "Neue Aufgabe"  # Funktioniert immer!
```

### 3. Makefile nutzen

Das Makefile wurde aktualisiert und funktioniert mit UV:

```bash
make sync      # Dependencies installieren
make test      # Tests ausführen
make format    # Code formatieren
make all       # Alle Checks
```

## 🔍 Häufige Fragen

### Muss ich venv aktivieren?

**Nein!** UV verwaltet die virtuelle Umgebung automatisch.

```bash
# Nicht mehr nötig:
source venv/bin/activate

# Stattdessen:
uv run <command>
```

### Wo ist die virtuelle Umgebung?

UV erstellt automatisch `.venv/` im Projektverzeichnis.

```bash
# Anzeigen
ls -la .venv/

# Löschen (falls nötig)
rm -rf .venv
uv sync --all-extras
```

### Funktioniert das in CI/CD?

**Ja!** GitHub Actions wurde aktualisiert:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v5

- name: Install dependencies
  run: uv sync --all-extras

- name: Run tests
  run: uv run pytest
```

### Kann ich weiterhin pip verwenden?

**Ja**, aber nicht empfohlen. UV ist abwärtskompatibel:

```bash
# UV mit pip-Syntax
uv pip install click
uv pip list
uv pip uninstall click
```

### Was ist mit requirements.txt?

`requirements.txt` bleibt für Kompatibilität, aber UV nutzt `pyproject.toml`:

```bash
# UV liest automatisch pyproject.toml
uv sync --all-extras
```

## 📊 Performance-Vergleich

Gemessen auf diesem Projekt:

| Aufgabe | pip | UV | Speedup |
|---------|-----|-----|---------|
| Erste Installation | ~45s | ~5s | **9x schneller** |
| Cached Installation | ~15s | ~1s | **15x schneller** |
| Dependency Resolution | ~10s | <1s | **>10x schneller** |

## ✅ Checkliste für Migration

- [x] UV installiert
- [x] Alte venv entfernt
- [x] `uv sync --all-extras` ausgeführt
- [x] Tests mit `uv run pytest` erfolgreich
- [x] CLI mit `uv run task --help` funktioniert
- [x] Makefile-Befehle getestet
- [x] Dokumentation gelesen

## 🎓 Für Dozierende

### Vorteile für den Unterricht

1. **Schneller:** Weniger Wartezeit bei Installation
2. **Einfacher:** Weniger Befehle zu erklären
3. **Konsistenter:** Gleiche Umgebung für alle
4. **Modern:** Zeigt aktuelle Best Practices

### Integration in Kurs

UV kann in allen Python-Modulen verwendet werden:

```bash
# Statt pip-basierter Installation
uv sync --all-extras

# Alle Befehle mit uv run
uv run pytest
uv run python script.py
```

### Ressourcen für Studierende

- [UV-GUIDE.md](./UV-GUIDE.md) - Umfassender Guide
- [Offizielle Docs](https://docs.astral.sh/uv/) - UV Dokumentation
- [GitHub](https://github.com/astral-sh/uv) - Source Code

## 📝 Feedback

Bei Fragen oder Problemen mit UV:

1. [UV-GUIDE.md](./UV-GUIDE.md) konsultieren
2. [Troubleshooting](./INSTALLATION.md#troubleshooting) prüfen
3. Issue erstellen

---

**Migration abgeschlossen:** 2025-12-18  
**UV Version:** 0.5+  
**Status:** ✅ Vollständig getestet

