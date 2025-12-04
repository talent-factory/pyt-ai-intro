# Troubleshooting - Git-Commit-System

Lösungen für häufige Probleme beim Verwenden des Git-Commit-Systems.

## Installation und Setup

### Problem: Python-Module nicht gefunden
```
ModuleNotFoundError: No module named 'pre_commit_checks'
```

**Lösung 1**: Aus dem Projektverzeichnis ausführen
```bash
cd /pfad/zum/projekt
python commit/commit.py
# oder
./commit.sh
```

**Lösung 2**: Python-Path setzen
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/commit"
python commit/commit.py
```

### Problem: Berechtigungen fehlen
```
Permission denied: ./commit.sh
```

**Lösung**: Ausführungsrechte setzen
```bash
chmod +x commit.sh
chmod +x commit/commit.py
```

## Pre-Commit-Checks

### Problem: Black nicht gefunden
```
⏭️ Code-Formatierung (Black): Tool nicht verfügbar
```

**Lösung**: Black installieren
```bash
# Mit pip
pip install black

# Mit uv (empfohlen)
uv add black --dev

# Global installieren
pip install --user black
```

### Problem: Ruff-Fehler
```
❌ Linting (Ruff): 15 Fehler gefunden
```

**Lösung 1**: Automatische Reparatur
```bash
ruff check --fix .
```

**Lösung 2**: Konfiguration anpassen
```toml
# pyproject.toml
[tool.ruff]
ignore = ["E501", "F401"]  # Lange Zeilen, ungenutzte Imports
```

**Lösung 3**: Spezifische Zeilen ignorieren
```python
import unused_module  # noqa: F401
very_long_line = "This line is too long but necessary"  # noqa: E501
```

### Problem: Tests schlagen fehl
```
❌ Tests (pytest): 3 failed, 12 passed
```

**Lösung 1**: Detaillierte Test-Ausgabe
```bash
pytest -v --tb=long
```

**Lösung 2**: Spezifische Tests ausführen
```bash
pytest tests/test_specific.py -v
```

**Lösung 3**: Tests temporär überspringen
```bash
./commit.sh --skip-tests
```

**Lösung 4**: Fehlgeschlagene Tests reparieren
```python
# Häufige Test-Probleme
def test_example():
    # Problem: Hardcoded Pfade
    # assert open("/absolute/path/file.txt")
    
    # Lösung: Relative Pfade
    from pathlib import Path
    test_file = Path(__file__).parent / "fixtures" / "file.txt"
    assert test_file.exists()
```

### Problem: mypy-Fehler
```
⚠️ Type-Checking (mypy): 5 Warnungen
```

**Lösung 1**: Type-Hints hinzufügen
```python
# Vorher
def calculate(x, y):
    return x + y

# Nachher
def calculate(x: int, y: int) -> int:
    return x + y
```

**Lösung 2**: mypy-Konfiguration
```toml
# pyproject.toml
[tool.mypy]
ignore_missing_imports = true
strict_optional = false
```

## Git-Probleme

### Problem: Keine Änderungen zum Committen
```
❌ Keine Änderungen zum Committen gefunden!
```

**Lösung 1**: Status prüfen
```bash
git status
```

**Lösung 2**: Dateien manuell hinzufügen
```bash
git add .
./commit.sh
```

**Lösung 3**: Untracked Files einschliessen
```bash
git add -A  # Alle Dateien inklusive gelöschte
./commit.sh
```

### Problem: Merge-Konflikte
```
error: Merging is not possible because you have unmerged files.
```

**Lösung**: Konflikte lösen vor Commit
```bash
# 1. Konflikte in Dateien lösen
git status  # Zeigt konfliktbehaftete Dateien

# 2. Dateien als gelöst markieren
git add konflikt_datei.py

# 3. Merge abschliessen
git commit -m "Merge-Konflikte gelöst"
# oder
./commit.sh -m "Merge-Konflikte gelöst"
```

### Problem: Detached HEAD
```
You are in 'detached HEAD' state.
```

**Lösung**: Zurück zum Branch
```bash
# Aktuellen Branch anzeigen
git branch

# Zu Branch wechseln
git checkout main
# oder
git checkout develop
```

## Performance-Probleme

### Problem: Checks dauern zu lange
```
⏰ Tests (pytest): Timeout (>5min)
```

**Lösung 1**: Tests optimieren
```python
# Langsame Tests markieren
import pytest

@pytest.mark.slow
def test_heavy_computation():
    pass

# Schnelle Tests ausführen
pytest -m "not slow"
```

**Lösung 2**: Parallele Test-Ausführung
```bash
# pytest-xdist installieren
pip install pytest-xdist

# Tests parallel ausführen
pytest -n auto
```

**Lösung 3**: Tests überspringen
```bash
./commit.sh --skip-tests
```

### Problem: Grosse Repositories
```
Linting dauert sehr lange bei 1000+ Dateien
```

**Lösung 1**: Nur geänderte Dateien prüfen
```bash
# Nur gestakte Dateien
ruff check $(git diff --cached --name-only --diff-filter=AM | grep '\.py$')
```

**Lösung 2**: Verzeichnisse ausschliessen
```toml
# pyproject.toml
[tool.ruff]
exclude = ["migrations/", "vendor/", "node_modules/"]
```

## Commit-Nachrichten

### Problem: Automatische Nachricht unpassend
```
✨ feat: 15 Dateien aktualisiert  # Zu generisch
```

**Lösung**: Eigene Nachricht verwenden
```bash
./commit.sh -m "Benutzer-Authentifizierung implementiert"
```

### Problem: Commit-Typ falsch erkannt
```
🧪 test: API-Endpunkt hinzugefügt  # Sollte "feat" sein
```

**Lösung**: Manuell korrigieren
```bash
./commit.sh -m "✨ feat: API-Endpunkt für Benutzerdaten hinzugefügt"
```

## Netzwerk-Probleme

### Problem: Push schlägt fehl
```
❌ Fehler beim Pushen!
fatal: unable to access 'https://github.com/...': Could not resolve host
```

**Lösung 1**: Netzwerkverbindung prüfen
```bash
ping github.com
```

**Lösung 2**: SSH statt HTTPS verwenden
```bash
git remote set-url origin git@github.com:user/repo.git
```

**Lösung 3**: Proxy-Konfiguration
```bash
git config --global http.proxy http://proxy.company.com:8080
```

### Problem: Authentication failed
```
remote: Invalid username or password.
```

**Lösung 1**: Personal Access Token verwenden
```bash
# GitHub Settings > Developer settings > Personal access tokens
git remote set-url origin https://username:token@github.com/user/repo.git
```

**Lösung 2**: SSH-Key konfigurieren
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Public Key zu GitHub hinzufügen
```

## Debugging

### Problem: Unbekannter Fehler
```
Unerwarteter Fehler im Commit-System
```

**Lösung 1**: Verbose-Modus aktivieren
```bash
python commit/commit.py --help  # Alle Optionen anzeigen
```

**Lösung 2**: Git-Befehle manuell ausführen
```bash
git status --porcelain
git diff --cached
git commit -m "Test-Commit"
```

**Lösung 3**: Python-Traceback anzeigen
```python
# In commit.py temporär hinzufügen
import traceback
try:
    # ... Code ...
except Exception as e:
    traceback.print_exc()
    raise
```

### Problem: Encoding-Fehler
```
UnicodeDecodeError: 'utf-8' codec can't decode byte
```

**Lösung**: Git-Encoding konfigurieren
```bash
git config --global core.quotepath false
git config --global core.precomposeunicode true
```

## Häufige Fehlermeldungen

### `fatal: not a git repository`
**Lösung**: In Git-Repository wechseln oder initialisieren
```bash
cd /pfad/zum/git/repo
# oder
git init
```

### `error: pathspec 'file.py' did not match any files`
**Lösung**: Dateiname und -pfad prüfen
```bash
git status  # Zeigt tatsächliche Dateinamen
```

### `fatal: refusing to merge unrelated histories`
**Lösung**: Force-Merge erlauben
```bash
git merge --allow-unrelated-histories
```

## Support und Hilfe

### Logs sammeln
```bash
# Git-Log der letzten Commits
git log --oneline -10

# System-Informationen
python --version
git --version
which python
which git
```

### Konfiguration prüfen
```bash
# Git-Konfiguration
git config --list

# Python-Module
pip list | grep -E "(black|ruff|pytest)"
```

### Reset bei Problemen
```bash
# Alle Änderungen verwerfen
git reset --hard HEAD

# Staging-Area leeren
git reset HEAD

# Letzten Commit rückgängig machen
git reset --soft HEAD~1
```
