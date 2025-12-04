# Commit-Typen - Emoji Conventional Commits

Alle Commit-Nachrichten verwenden das **Emoji Conventional Commit Format** mit deutschen Beschreibungen.

## Format

```
<emoji> <typ>: <beschreibung>

[optional body]

[optional footer]
```

## Haupttypen

### ✨ feat - Neue Funktionalität
Neue Features oder Funktionen hinzufügen.

**Beispiele:**
- ✨ feat: Benutzer-Registrierung hinzugefügt
- ✨ feat: API-Endpunkt für Datenexport implementiert
- ✨ feat: Dark Mode für UI hinzugefügt

### 🐛 fix - Fehlerbehebung
Bugs und Fehler beheben.

**Beispiele:**
- 🐛 fix: Null-Pointer-Exception in Login behoben
- 🐛 fix: Falsche Berechnung in Preiskalkulierung korrigiert
- 🐛 fix: Memory Leak in Datenverarbeitung behoben

### 📚 docs - Dokumentation
Dokumentation hinzufügen oder aktualisieren.

**Beispiele:**
- 📚 docs: README mit Installationsanleitung aktualisiert
- 📚 docs: API-Dokumentation für neue Endpunkte hinzugefügt
- 📚 docs: Code-Kommentare für komplexe Algorithmen ergänzt

### 💎 style - Code-Formatierung
Code-Stil, Formatierung, Leerzeichen (keine Logik-Änderungen).

**Beispiele:**
- 💎 style: Code mit Black formatiert
- 💎 style: Import-Reihenfolge korrigiert
- 💎 style: Einrückung und Leerzeichen bereinigt

### ♻️ refactor - Code-Umstrukturierung
Code umstrukturieren ohne Funktionalität zu ändern.

**Beispiele:**
- ♻️ refactor: Datenbankzugriff in separate Klasse extrahiert
- ♻️ refactor: Komplexe Funktion in kleinere Teile aufgeteilt
- ♻️ refactor: Doppelten Code in Utility-Funktion zusammengefasst

### ⚡ perf - Performance-Verbesserungen
Performance und Geschwindigkeit optimieren.

**Beispiele:**
- ⚡ perf: Datenbankabfragen optimiert
- ⚡ perf: Caching für häufige Berechnungen hinzugefügt
- ⚡ perf: Algorithmus von O(n²) auf O(n log n) verbessert

### 🧪 test - Tests
Tests hinzufügen, korrigieren oder verbessern.

**Beispiele:**
- 🧪 test: Unit-Tests für Benutzer-Service hinzugefügt
- 🧪 test: Integration-Tests für API-Endpunkte erweitert
- 🧪 test: Flaky Test für Datenbankverbindung repariert

### 🔧 chore - Build und Tools
Build-System, Tools, Konfiguration, Dependencies.

**Beispiele:**
- 🔧 chore: Dependencies auf neueste Versionen aktualisiert
- 🔧 chore: CI/CD-Pipeline für automatische Tests hinzugefügt
- 🔧 chore: Docker-Konfiguration für Entwicklungsumgebung erstellt

## Weitere Typen

### 🚀 deploy - Deployment
Deployment-bezogene Änderungen.

**Beispiele:**
- 🚀 deploy: Produktionsumgebung für Version 2.0 konfiguriert
- 🚀 deploy: Kubernetes-Manifeste für Staging-Umgebung hinzugefügt

### 🔒 security - Sicherheit
Sicherheitslücken beheben oder Sicherheit verbessern.

**Beispiele:**
- 🔒 security: SQL-Injection-Schwachstelle behoben
- 🔒 security: Passwort-Hashing auf bcrypt umgestellt

### 🌐 i18n - Internationalisierung
Übersetzungen und Lokalisierung.

**Beispiele:**
- 🌐 i18n: Deutsche Übersetzungen für UI hinzugefügt
- 🌐 i18n: Datumsformatierung für verschiedene Locales implementiert

### 📱 ui - User Interface
UI/UX-Verbesserungen und Design-Änderungen.

**Beispiele:**
- 📱 ui: Responsive Design für mobile Geräte verbessert
- 📱 ui: Neue Icons und Farbschema implementiert

### 🗃️ db - Datenbank
Datenbank-Migrationen und Schema-Änderungen.

**Beispiele:**
- 🗃️ db: Migration für neue Benutzer-Tabelle hinzugefügt
- 🗃️ db: Index für bessere Query-Performance erstellt

### 🔥 remove - Code entfernen
Toten Code, veraltete Features oder Dateien entfernen.

**Beispiele:**
- 🔥 remove: Veraltete API-Endpunkte entfernt
- 🔥 remove: Nicht verwendete Dependencies aus package.json entfernt

### 🚨 breaking - Breaking Changes
Änderungen, die bestehende Funktionalität brechen.

**Beispiele:**
- 🚨 breaking: API-Endpunkt-URLs von v1 auf v2 geändert
- 🚨 breaking: Datenbank-Schema für Benutzer-Tabelle überarbeitet

## Automatische Typerkennung

Das Commit-System erkennt automatisch den passenden Typ basierend auf:

- **Dateiendungen**: `.py`, `.js`, `.md`, `.json`, etc.
- **Verzeichnissen**: `tests/`, `docs/`, `src/`, etc.
- **Änderungsmustern**: Neue Dateien, gelöschte Dateien, etc.
- **Schlüsselwörtern**: "fix", "add", "remove", "update", etc.

## Regeln

1. **Imperativ**: Verwende imperative Form ("hinzufügen" statt "hinzugefügt")
2. **Deutsch**: Alle Beschreibungen in deutscher Sprache
3. **Kurz**: Erste Zeile max. 50 Zeichen
4. **Präzise**: Beschreibe WAS geändert wurde, nicht WIE
5. **Konsistent**: Verwende einheitliche Terminologie

## Beispiel-Commits

```
✨ feat: Passwort-Reset-Funktionalität hinzugefügt

Benutzer können jetzt ihr Passwort über E-Mail zurücksetzen.
Implementiert sichere Token-Generierung und E-Mail-Versand.

Closes #123
```

```
🐛 fix: Speicher-Leak in Bildverarbeitung behoben

Bilder wurden nach Verarbeitung nicht korrekt freigegeben.
Implementiert explizite Speicherbereinigung nach jedem Vorgang.

Fixes #456
```

```
📚 docs: API-Dokumentation für Authentifizierung erweitert

- Beispiele für JWT-Token-Verwendung hinzugefügt
- Fehlerbehandlung für ungültige Credentials dokumentiert
- Swagger-Definitionen aktualisiert
```
