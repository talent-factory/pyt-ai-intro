# Best Practices - Git-Commit-System

Bewährte Praktiken für professionelle Git-Commits mit dem automatisierten Commit-System.

## Commit-Häufigkeit

### ✅ Häufig committen
- **Regel**: Mindestens einmal täglich committen
- **Vorteil**: Kleinere, verständlichere Änderungen
- **Beispiel**: Nach jeder abgeschlossenen Funktion oder Bugfix

### ✅ Logische Einheiten
- **Ein Commit = Eine logische Änderung**
- **Schlecht**: Bugfix + neue Funktion + Dokumentation
- **Gut**: Drei separate Commits

```bash
# Schlecht
✨ feat: Login-System und Bugfix und Docs

# Gut  
🐛 fix: Null-Pointer-Exception in Login behoben
✨ feat: Passwort-Reset-Funktionalität hinzugefügt
📚 docs: API-Dokumentation für Authentifizierung erweitert
```

## Commit-Nachrichten

### Format-Regeln
1. **Imperativ**: "hinzufügen" statt "hinzugefügt"
2. **Deutsch**: Alle Beschreibungen in deutscher Sprache
3. **Präzise**: WAS wurde geändert, nicht WIE
4. **Kurz**: Erste Zeile maximal 50 Zeichen

### Gute Beispiele
```
✨ feat: Benutzer-Registrierung hinzugefügt
🐛 fix: Memory Leak in Bildverarbeitung behoben
📚 docs: Installation-Guide für Windows ergänzt
♻️ refactor: Datenbankzugriff in Service-Klasse extrahiert
🧪 test: Unit-Tests für Passwort-Validierung hinzugefügt
```

### Schlechte Beispiele
```
❌ fix stuff                           # Zu unspezifisch
❌ Added new feature                   # Englisch statt Deutsch
❌ Benutzer-Registrierung hinzugefügt  # Kein Emoji/Typ
❌ 🐛 fix: Fehler wurde behoben        # Nicht imperativ
```

## Pre-Commit-Checks

### Immer ausführen
- **Code-Formatierung**: Black, Prettier
- **Linting**: Ruff, ESLint
- **Kompilierung**: Stelle sicher, dass Code kompiliert

### Selektiv überspringen
```bash
# Nur bei Notfällen
./commit.sh --no-verify

# Tests überspringen bei WIP
./commit.sh --skip-tests
```

### Check-Reihenfolge optimieren
1. **Schnelle Checks zuerst**: Formatierung (< 1s)
2. **Mittlere Checks**: Linting (1-5s)
3. **Langsame Checks**: Tests (5-60s)

## Branch-Strategien

### Feature-Branches
```bash
# Neues Feature
git checkout -b feature/user-registration
# ... Entwicklung ...
./commit.sh -m "Benutzer-Registrierung implementiert"
git push origin feature/user-registration
```

### Hotfix-Branches
```bash
# Kritischer Bugfix
git checkout -b hotfix/login-crash
# ... Bugfix ...
./commit.sh -m "Kritischen Login-Crash behoben"
git push origin hotfix/login-crash
```

## Commit-Aufteilung

### Wann aufteilen?
- **Verschiedene Bereiche**: UI + Backend + Tests
- **Verschiedene Typen**: Bugfix + neue Funktion
- **Grosse Änderungen**: > 20 Dateien oder > 500 Zeilen

### Wie aufteilen?
```bash
# Schritt 1: Nur UI-Änderungen stagen
git add src/components/
./commit.sh -m "UI-Komponenten für Login überarbeitet"

# Schritt 2: Backend-Änderungen
git add src/api/
./commit.sh -m "API-Endpunkt für Authentifizierung erweitert"

# Schritt 3: Tests
git add tests/
./commit.sh -m "Tests für neue Login-Funktionalität hinzugefügt"
```

## Code-Review-Vorbereitung

### Vor dem Push
1. **Commit-Historie prüfen**: `git log --oneline -10`
2. **Diff reviewen**: `git diff HEAD~1`
3. **Tests lokal ausführen**: `pytest` oder `npm test`

### Commit-Nachrichten für Reviewer
```bash
# Gut: Kontext für Reviewer
✨ feat: OAuth2-Integration für Google Login

Implementiert OAuth2-Flow für Google-Authentifizierung.
Benutzer können sich jetzt mit Google-Account anmelden.

- Neue OAuth2-Service-Klasse
- Frontend-Integration mit Google-Button
- Fehlerbehandlung für ungültige Tokens

Closes #123
```

## Performance-Optimierung

### Grosse Repositories
- **Selective Staging**: Nur relevante Dateien stagen
- **Parallele Checks**: System nutzt automatisch parallele Ausführung
- **Cache nutzen**: Tools wie pytest, ruff nutzen eigene Caches

### CI/CD-Integration
```yaml
# .github/workflows/commit-checks.yml
name: Commit Checks
on: [push, pull_request]
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements-dev.txt
      - name: Run commit checks
        run: python commit/pre_commit_checks.py
```

## Fehlerbehandlung

### Häufige Probleme

**Problem**: Tests schlagen fehl
```bash
# Lösung 1: Tests reparieren
pytest -v  # Detaillierte Ausgabe
# ... Tests reparieren ...
./commit.sh

# Lösung 2: Tests temporär überspringen (nur bei WIP)
./commit.sh --skip-tests
```

**Problem**: Code-Formatierung
```bash
# Automatisch reparieren
black .
ruff check --fix .
./commit.sh
```

**Problem**: Merge-Konflikte
```bash
# Nach Konflikt-Lösung
git add .
./commit.sh -m "Merge-Konflikte in Feature-Branch gelöst"
```

## Team-Konventionen

### Einheitliche Standards
- **Commit-Typen**: Team einigt sich auf Subset der verfügbaren Typen
- **Scopes**: Projektspezifische Scopes definieren (api, ui, db, etc.)
- **Breaking Changes**: Klare Kennzeichnung mit 🚨 breaking

### Beispiel-Konventionen
```bash
# Scopes für Web-App
✨ feat(api): Neuer Endpunkt für Benutzerdaten
📱 ui(login): Responsive Design für mobile Geräte
🗃️ db(users): Migration für erweiterte Benutzer-Tabelle

# Breaking Changes
🚨 breaking(api): Endpunkt /users/list zu /api/v2/users geändert

BREAKING CHANGE: API-Endpunkt-URLs von v1 auf v2 migriert.
Alle Client-Anwendungen müssen URLs aktualisieren.
```

## Automatisierung

### Git-Hooks
```bash
# .git/hooks/pre-commit
#!/bin/bash
python commit/pre_commit_checks.py
```

### IDE-Integration
- **VS Code**: Tasks für Commit-System
- **PyCharm**: External Tools konfigurieren
- **Vim/Neovim**: Shortcuts für Commit-Befehle

### Alias erstellen
```bash
# ~/.bashrc oder ~/.zshrc
alias commit='./commit.sh'
alias commit-quick='./commit.sh --skip-tests'
alias commit-force='./commit.sh --no-verify'
```

## Monitoring und Metriken

### Commit-Qualität messen
- **Commit-Häufigkeit**: Täglich committen
- **Commit-Grösse**: < 20 Dateien pro Commit
- **Test-Coverage**: Mindestens 80% nach Commits
- **Build-Erfolg**: Alle Commits sollten CI/CD bestehen

### Tools für Analyse
```bash
# Commit-Statistiken
git log --oneline --since="1 month ago" | wc -l

# Grösste Commits finden
git log --stat --since="1 month ago" | grep -E "files? changed"

# Häufigste Commit-Typen
git log --oneline --since="1 month ago" | grep -oE "^[^:]*:" | sort | uniq -c
```
