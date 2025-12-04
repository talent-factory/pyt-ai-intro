# Pre-Commit-Checks - Automatische Qualitätsprüfungen

Das Commit-System führt automatische Qualitätschecks basierend auf dem erkannten Projekttyp durch.

## Projekterkennung

Das System erkennt automatisch den Projekttyp anhand von:

- **Python**: `pyproject.toml`, `requirements.txt`, `setup.py`, `.py`-Dateien
- **Java**: `pom.xml`, `build.gradle`, `gradle.properties`, `.java`-Dateien  
- **React/Node.js**: `package.json`, `tsconfig.json`, `.js/.ts/.jsx/.tsx`-Dateien
- **Dokumentation**: `.md`, `.tex`, `.adoc`-Dateien

## Python-Projekt-Checks

### 1. Code-Formatierung (Black)
```bash
black --check --diff .
```
- Prüft Python-Code-Formatierung
- Zeigt Unterschiede an falls nicht formatiert
- **Fehler**: Stoppt Commit, schlägt `black .` vor

### 2. Linting (Ruff)
```bash
ruff check .
```
- Prüft Code-Qualität und Style-Violations
- Erkennt potentielle Bugs und Code-Smells
- **Fehler**: Stoppt Commit, zeigt Probleme an

### 3. Type-Checking (mypy) - Optional
```bash
mypy . --ignore-missing-imports
```
- Prüft Type-Hints und Type-Safety
- Nur wenn `mypy` in Dependencies gefunden
- **Fehler**: Warnung, stoppt Commit nicht

### 4. Tests (pytest)
```bash
pytest --tb=short -q
```
- Führt alle Tests aus
- Kurze Ausgabe bei Fehlern
- **Fehler**: Stoppt Commit, zeigt fehlgeschlagene Tests

### 5. Import-Sortierung (isort) - Optional
```bash
isort --check-only --diff .
```
- Prüft Import-Reihenfolge
- Nur wenn `isort` in Dependencies
- **Fehler**: Stoppt Commit, schlägt `isort .` vor

## Java-Projekt-Checks

### Maven-Projekte

#### 1. Kompilierung
```bash
mvn compile -q
```
- Kompiliert Java-Quellcode
- **Fehler**: Stoppt Commit, zeigt Compiler-Fehler

#### 2. Tests
```bash
mvn test -q
```
- Führt JUnit-Tests aus
- **Fehler**: Stoppt Commit, zeigt fehlgeschlagene Tests

#### 3. Code-Style (Checkstyle) - Optional
```bash
mvn checkstyle:check -q
```
- Prüft Code-Style-Konventionen
- Nur wenn Checkstyle-Plugin konfiguriert
- **Fehler**: Warnung, stoppt Commit nicht

### Gradle-Projekte

#### 1. Kompilierung
```bash
./gradlew compileJava -q
```
- Kompiliert Java-Quellcode
- **Fehler**: Stoppt Commit, zeigt Compiler-Fehler

#### 2. Tests
```bash
./gradlew test -q
```
- Führt Tests aus
- **Fehler**: Stoppt Commit, zeigt fehlgeschlagene Tests

## React/Node.js-Projekt-Checks

### 1. Linting (ESLint)
```bash
npm run lint
# oder
yarn lint
```
- Prüft JavaScript/TypeScript-Code-Qualität
- **Fehler**: Stoppt Commit, zeigt Linting-Probleme

### 2. Type-Checking (TypeScript)
```bash
npx tsc --noEmit
```
- Prüft TypeScript-Typen
- Nur bei TypeScript-Projekten
- **Fehler**: Stoppt Commit, zeigt Type-Fehler

### 3. Formatierung (Prettier)
```bash
npx prettier --check .
```
- Prüft Code-Formatierung
- **Fehler**: Stoppt Commit, schlägt `prettier --write .` vor

### 4. Tests (Jest/Vitest)
```bash
npm test -- --passWithNoTests
# oder
yarn test --passWithNoTests
```
- Führt JavaScript/TypeScript-Tests aus
- **Fehler**: Stoppt Commit, zeigt fehlgeschlagene Tests

### 5. Build-Test
```bash
npm run build
# oder  
yarn build
```
- Testet ob Projekt erfolgreich gebaut werden kann
- **Fehler**: Stoppt Commit, zeigt Build-Fehler

## Dokumentations-Checks

### 1. Markdown-Linting (markdownlint) - Optional
```bash
markdownlint **/*.md
```
- Prüft Markdown-Syntax und Style
- Nur wenn `markdownlint` verfügbar
- **Fehler**: Warnung, stoppt Commit nicht

### 2. LaTeX-Kompilierung - Optional
```bash
pdflatex -interaction=nonstopmode document.tex
```
- Kompiliert LaTeX-Dokumente
- Nur bei `.tex`-Dateien
- **Fehler**: Warnung, stoppt Commit nicht

## Check-Konfiguration

### Überspringen von Checks
```bash
/commit --no-verify     # Alle Checks überspringen
/commit --skip-tests    # Nur Tests überspringen
```

### Check-Reihenfolge
1. **Schnelle Checks zuerst**: Formatierung, Linting
2. **Langsamere Checks**: Type-Checking, Kompilierung  
3. **Tests zuletzt**: Oft am langsamsten

### Fehlerbehandlung
- **Kritische Fehler**: Stoppen Commit (Kompilierung, Tests)
- **Style-Fehler**: Stoppen Commit mit Fix-Vorschlägen
- **Warnungen**: Zeigen Meldung, Commit läuft weiter

## Ausgabe-Format

### Erfolgreiche Checks
```
✅ Code-Formatierung (Black): OK
✅ Linting (Ruff): OK  
✅ Tests (pytest): 15 passed
```

### Fehlgeschlagene Checks
```
❌ Code-Formatierung (Black): 3 Dateien nicht formatiert
   Lösung: black .

❌ Tests (pytest): 2 failed, 13 passed
   test_user.py::test_login FAILED
   test_api.py::test_auth FAILED
```

### Übersprungene Checks
```
⏭️ Type-Checking (mypy): Nicht verfügbar
⏭️ Tests: Übersprungen (--skip-tests)
```

## Performance-Optimierung

### Parallele Ausführung
- Unabhängige Checks laufen parallel
- Reduziert Gesamtzeit um 30-50%

### Caching
- Nutzt Tool-eigene Caches (pytest, ruff, etc.)
- Wiederverwendung von Kompilierungs-Artefakten

### Inkrementelle Checks
- Nur geänderte Dateien prüfen (wo möglich)
- Besonders effektiv bei grossen Projekten

## Troubleshooting

### Häufige Probleme

**Problem**: `black` nicht gefunden
**Lösung**: `pip install black` oder `uv add black --dev`

**Problem**: Tests schlagen fehl
**Lösung**: Tests lokal ausführen und reparieren vor Commit

**Problem**: Checks zu langsam
**Lösung**: `--skip-tests` verwenden oder Tests optimieren

**Problem**: False Positives bei Linting
**Lösung**: Konfigurationsdateien anpassen (`.ruff.toml`, `.eslintrc`)
