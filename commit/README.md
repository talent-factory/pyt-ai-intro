# Git-Commit-System

Professionelles Git-Commit-System mit automatischen Qualitätschecks und konventionellen Commit-Nachrichten in deutscher Sprache.

## ✨ Features

- 🤖 **Automatische Commit-Typerkennung** basierend auf Dateiänderungen
- 🔍 **Pre-Commit-Checks** für Python, Java, React/Node.js
- 🇩🇪 **Deutsche Commit-Nachrichten** im Emoji Conventional Commit Format
- ⚡ **Parallele Check-Ausführung** für bessere Performance
- 📋 **Intelligente Staging-Analyse** mit Aufteilungsvorschlägen
- 🚀 **Integrierter Push-Workflow** mit Sicherheitsabfragen

## 🚀 Schnellstart

### Installation

Das System ist bereits im Projekt integriert. Keine zusätzliche Installation nötig.

### Verwendung

```bash
# Standard-Commit mit allen Checks
./commit.sh

# Mit Optionen
./commit.sh --no-verify     # Überspringt Pre-Commit-Checks
./commit.sh --skip-tests    # Überspringt Tests
./commit.sh --force-push    # Führt force push aus
./commit.sh -m "Eigene Nachricht"  # Eigene Commit-Nachricht
```

### Beispiel-Session

```bash
$ ./commit.sh

🚀 Git-Commit-System gestartet
==================================================

🐍 Python-Projekt erkannt - führe Qualitätschecks durch...
   ✅ Code-Formatierung (Black): OK
   ✅ Linting (Ruff): OK
   ✅ Tests (pytest): 15 passed

📁 Schritt 2: Staging-Analyse
📦 3 ungestakte Änderungen gefunden
   Füge automatisch alle Änderungen hinzu...
📋 3 Dateien zum Committen:
   • commit/commit.py
   • commit/pre_commit_checks.py
   • README.md

📝 Schritt 3: Commit-Nachricht generieren
📋 Vorgeschlagene Commit-Nachricht:
----------------------------------------
✨ feat: Git-Commit-System implementiert
----------------------------------------

💾 Schritt 4: Commit erstellen
✅ Commit erfolgreich erstellt!
   Commit-Hash: a1b2c3d

🌐 Schritt 5: Push zum Remote-Repository
Push zum Remote-Repository? (j/N): j
✅ Änderungen erfolgreich gepusht!
```

## 📋 Unterstützte Projekttypen

### Python-Projekte
- **Erkennung**: `pyproject.toml`, `requirements.txt`, `.py`-Dateien
- **Checks**: Black, Ruff, pytest, mypy (optional)
- **Konfiguration**: Nutzt bestehende Tool-Konfigurationen

### Java-Projekte
- **Erkennung**: `pom.xml`, `build.gradle`, `.java`-Dateien
- **Checks**: Maven/Gradle compile, Tests, Checkstyle (optional)
- **Build-Tools**: Maven und Gradle unterstützt

### React/Node.js-Projekte
- **Erkennung**: `package.json`, `.js/.ts`-Dateien
- **Checks**: ESLint, TypeScript, Prettier, Jest/Vitest
- **Package-Manager**: npm und yarn unterstützt

### Dokumentation
- **Erkennung**: `.md`, `.tex`-Dateien
- **Checks**: Markdown-Linting (optional), LaTeX-Kompilierung

## 🎯 Commit-Typen

Das System verwendet Emoji Conventional Commits mit deutschen Beschreibungen:

| Emoji | Typ | Beschreibung | Beispiel |
|-------|-----|--------------|----------|
| ✨ | `feat` | Neue Funktionalität | `✨ feat: Benutzer-Registrierung hinzugefügt` |
| 🐛 | `fix` | Fehlerbehebung | `🐛 fix: Null-Pointer-Exception behoben` |
| 📚 | `docs` | Dokumentation | `📚 docs: API-Dokumentation erweitert` |
| 💎 | `style` | Code-Formatierung | `💎 style: Code mit Black formatiert` |
| ♻️ | `refactor` | Code-Umstrukturierung | `♻️ refactor: Service-Klasse extrahiert` |
| ⚡ | `perf` | Performance | `⚡ perf: Datenbankabfragen optimiert` |
| 🧪 | `test` | Tests | `🧪 test: Unit-Tests hinzugefügt` |
| 🔧 | `chore` | Build/Tools | `🔧 chore: Dependencies aktualisiert` |

**Vollständige Liste**: [commit-types.md](commit-types.md)

## ⚙️ Konfiguration

### Pre-Commit-Checks anpassen

Das System erkennt automatisch verfügbare Tools. Konfiguration über Standard-Dateien:

```toml
# pyproject.toml - Python-Konfiguration
[tool.ruff]
line-length = 88
ignore = ["E501"]

[tool.black]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Checks überspringen

```bash
# Alle Checks überspringen (Notfall)
./commit.sh --no-verify

# Nur Tests überspringen (bei WIP)
./commit.sh --skip-tests
```

## 📁 Projektstruktur

```
commit/
├── commit.py                    # Hauptskript
├── pre_commit_checks.py         # Pre-Commit-Checks
├── commit_message_generator.py  # Nachrichtengenerierung
├── commit-types.md             # Commit-Typen-Referenz
├── pre-commit-checks.md        # Check-Dokumentation
├── best-practices.md           # Best Practices
├── troubleshooting.md          # Problemlösungen
└── README.md                   # Diese Datei

commit.sh                       # Shell-Wrapper
```

## 🔧 Erweiterte Verwendung

### Eigene Commit-Nachrichten

```bash
# Kurze Nachricht
./commit.sh -m "Bugfix für Login-Problem"

# Vollständige Conventional Commit Nachricht
./commit.sh -m "🐛 fix(auth): Session-Timeout-Problem behoben

Benutzer wurden nach 5 Minuten automatisch ausgeloggt.
Timeout auf 30 Minuten erhöht und Warnung hinzugefügt.

Fixes #123"
```

### Batch-Commits

```bash
# Mehrere logische Änderungen aufteilen
git add src/api/
./commit.sh -m "API-Endpunkte erweitert"

git add src/ui/
./commit.sh -m "UI-Komponenten aktualisiert"

git add tests/
./commit.sh -m "Tests für neue Features hinzugefügt"
```

### CI/CD-Integration

```yaml
# .github/workflows/commit-checks.yml
name: Commit Quality Checks
on: [push, pull_request]

jobs:
  quality-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements-dev.txt
      - name: Run pre-commit checks
        run: python commit/pre_commit_checks.py
```

## 📚 Dokumentation

- **[Commit-Typen](commit-types.md)**: Vollständige Referenz aller Commit-Typen
- **[Pre-Commit-Checks](pre-commit-checks.md)**: Details zu automatischen Checks
- **[Best Practices](best-practices.md)**: Bewährte Praktiken für Git-Commits
- **[Troubleshooting](troubleshooting.md)**: Lösungen für häufige Probleme

## 🤝 Beitragen

Das System ist für das Projekt `pyt-ai-intro` optimiert, kann aber für andere Projekte angepasst werden:

1. **Projekttyp-Erkennung** in `pre_commit_checks.py` erweitern
2. **Neue Commit-Typen** in `commit_message_generator.py` hinzufügen
3. **Spezifische Checks** für Projektanforderungen implementieren

## 📄 Lizenz

Teil des `pyt-ai-intro` Kursprojekts. Für Bildungszwecke entwickelt.

---

**Wichtiger Hinweis**: Alle Commit-Nachrichten werden in deutscher Sprache erstellt und enthalten KEINE automatischen Signaturen wie "Generated with Claude Code" oder "Co-Authored-By".
