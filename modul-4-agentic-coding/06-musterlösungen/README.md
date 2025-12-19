# Musterlösungen - Modul 4: Agentic Coding

Dieses Verzeichnis enthält vollständige Musterlösungen für die Nachbearbeitungsaufgaben des Moduls "Agentic Coding".

> **⚡ Wichtig:** Alle Musterlösungen verwenden **UV** als Package Manager statt pip. UV ist schneller, moderner und einfacher zu verwenden. Siehe [UV-GUIDE.md](./aufgabe-1/UV-GUIDE.md) für Details.

## 📁 Struktur

```
06-musterlösungen/
├── aufgabe-1/          # CLI-Tool: Task Manager
│   ├── task_manager/   # Hauptpaket
│   ├── tests/          # Test-Suite
│   ├── .github/        # CI/CD
│   ├── README.md       # Dokumentation
│   └── ...
└── README.md           # Diese Datei
```

## 🎯 Verfügbare Musterlösungen

### Aufgabe 1: CLI-Tool - Task Manager

**Status:** ✅ Vollständig

**Beschreibung:** Ein vollständiges Command-Line Tool für Task-Verwaltung mit allen geforderten Features.

**Features:**
- 5 CLI-Commands (add, list, complete, delete, stats)
- Click-Framework für Argument-Parsing
- JSON-basierte Persistenz
- Umfassende Fehlerbehandlung
- Strukturiertes Logging
- Type Hints und Docstrings
- Vollständige Test-Suite (pytest)
- CI/CD mit GitHub Actions

**Bewertung:** 35/35 Punkte

**Dokumentation:**
- [README.md](./aufgabe-1/README.md) - Vollständige Projektdokumentation
- [LÖSUNGSHINWEISE.md](./aufgabe-1/LÖSUNGSHINWEISE.md) - Detaillierte Erklärungen

**Schnellstart:**
```bash
cd aufgabe-1
uv sync --all-extras
uv run task --help
```

## 🎓 Verwendung der Musterlösungen

### Für Studierende

Die Musterlösungen dienen als:

1. **Referenz:** Beispiel für professionelle Code-Qualität
2. **Lernmaterial:** Best Practices und Patterns
3. **Vergleich:** Abgleich mit eigener Lösung
4. **Inspiration:** Ideen für Erweiterungen

**Wichtig:** Die Musterlösungen sollten erst nach eigener Bearbeitung der Aufgaben konsultiert werden!

### Für Dozierende

Die Musterlösungen bieten:

1. **Bewertungsgrundlage:** Klare Kriterien und Erwartungen
2. **Diskussionsgrundlage:** Basis für Code-Reviews
3. **Erweiterbarkeit:** Ausgangspunkt für weitere Aufgaben
4. **Qualitätsstandard:** Beispiel für erwartete Code-Qualität

## 📊 Bewertungskriterien

Alle Musterlösungen erfüllen die folgenden Kriterien:

| Kriterium | Gewichtung | Details |
|-----------|------------|---------|
| **Funktionalität** | 30% | Alle geforderten Features implementiert |
| **Code-Qualität** | 25% | Type Hints, Docstrings, Clean Code |
| **Tests** | 20% | Unit Tests, Coverage > 80% |
| **Dokumentation** | 15% | README, Kommentare, Docstrings |
| **CI/CD** | 10% | Automatisierte Tests und Builds |

## 🔧 Technische Standards

Alle Musterlösungen folgen diesen Standards:

### Python-Version
- Python 3.11 oder höher
- Kompatibilität mit 3.12

### Code-Qualität
- **Type Hints:** Vollständige Typisierung
- **Docstrings:** Google-Style für alle Funktionen
- **Formatierung:** Black (line-length=100)
- **Linting:** Flake8
- **Type Checking:** Mypy

### Testing
- **Framework:** pytest
- **Coverage:** Mindestens 80%
- **Fixtures:** Für Setup/Teardown
- **Isolation:** Keine Test-Abhängigkeiten

### CI/CD
- **Platform:** GitHub Actions
- **Matrix:** Mehrere OS und Python-Versionen
- **Checks:** Tests, Linting, Type-Checking
- **Artifacts:** Build-Artefakte

## 📚 Lernziele

Die Musterlösungen demonstrieren:

1. **Professionelle Entwicklung**
   - Projektstruktur
   - Dependency Management
   - Versionskontrolle

2. **Code-Qualität**
   - [Clean Code Prinzipien](https://de.wikipedia.org/wiki/Clean_Code)
   - [SOLID Prinzipien](https://de.wikipedia.org/wiki/Prinzipien_objektorientierten_Designs)
   - [Design Patterns](https://de.wikipedia.org/wiki/Entwurfsmuster)

3. **Testing**
   - Unit Testing
   - Test-Driven Development
   - Coverage-Analyse

4. **DevOps**
   - CI/CD Pipelines
   - Automatisierung
   - Build-Prozesse

5. **Dokumentation**
   - README-Struktur
   - Code-Kommentare
   - API-Dokumentation

## 🚀 Schnellstart

### Voraussetzungen

```bash
# Python-Version prüfen
python3 --version  # Sollte >= 3.11 sein

# UV installieren
curl -LsSf https://astral.sh/uv/install.sh | sh

# UV-Version prüfen
uv --version
```

### Installation

```bash
# In Musterlösungs-Verzeichnis wechseln
cd modul-4-agentic-coding/06-musterlösungen/aufgabe-1

# Dependencies installieren
uv sync --all-extras
```

### Tests ausführen

```bash
# Alle Tests
uv run pytest

# Mit Coverage
uv run pytest --cov=task_manager --cov-report=html

# Spezifische Tests
uv run pytest tests/test_cli.py
```

### Code-Qualität prüfen

```bash
# Formatierung
uv run black task_manager tests

# Linting
uv run flake8 task_manager

# Type Checking
uv run mypy task_manager
```

## 💡 Tipps für Studierende

### Vor der Bearbeitung

1. ✅ Aufgabenstellung genau lesen
2. ✅ Anforderungen verstehen
3. ✅ Eigene Lösung planen
4. ❌ Musterlösung NICHT ansehen

### Während der Bearbeitung

1. ✅ Schritt für Schritt vorgehen
2. ✅ Tests schreiben
3. ✅ Regelmässig committen
4. ❌ Musterlösung NICHT kopieren

### Nach der Bearbeitung

1. ✅ Eigene Lösung testen
2. ✅ Musterlösung vergleichen
3. ✅ Unterschiede analysieren
4. ✅ Verbesserungen identifizieren

## 🤝 Beitragen

Verbesserungsvorschläge für die Musterlösungen sind willkommen!

1. Issue erstellen mit Beschreibung
2. Fork erstellen
3. Änderungen implementieren
4. Pull Request erstellen

## 📝 Lizenz

MIT License - siehe LICENSE-Datei für Details.

## 👥 Autoren

Talent Factory - Python Training Team

---

**Zurück zu:** [Modul 4 README](../README.md)

