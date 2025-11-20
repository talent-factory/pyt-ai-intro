# Claude Code Präferenzen

## Sprache und Schreibweise

### Schweizer Schreibweise
Dieses Projekt verwendet die **Schweizer Schreibweise** (Schweizer Hochdeutsch).

**Wichtigste Regel:**
- ❌ Verwende KEIN 'ß' (Eszett/scharfes S)
- ✅ Verwende stattdessen 'ss' (Doppel-S)

**Beispiele:**
- ❌ `Straße` → ✅ `Strasse`
- ❌ `groß` → ✅ `gross`
- ❌ `heißt` → ✅ `heisst`
- ❌ `außer` → ✅ `ausser`
- ❌ `schließen` → ✅ `schliessen`

**Anwendung:**
- Alle Markdown-Dokumente (.md)
- Alle Python-Docstrings
- Alle Kommentare im Code
- Alle Variablennamen und Strings

## Weitere Konventionen

### Dokumentation
- Nutze klare, einfache Sprache
- Verwende Beispiele zur Veranschaulichung
- Strukturiere Inhalte mit Überschriften und Listen

### Code-Stil
- Python-Code folgt PEP 8
- Type Hints verwenden
- Docstrings für alle Funktionen
- Kommentare in Deutsch (Schweizer Schreibweise)

## Markdown-Konventionen

### Code-Block-Syntax

**Wichtige Regel: Code-Block-Ender**

Code-Blöcke in Markdown müssen IMMER mit ``` (drei Backticks) enden, NICHT mit ```text.

**Korrekt ✅:**

````markdown
```bash
python --version
```
````

**Falsch ❌:**

````markdown
```bash
python --version
```text
````

**Hintergrund:**

- Code-Blöcke beginnen mit ```<sprache> (z.B. ```bash, ```python, ```json)
- Code-Blöcke enden mit ``` (OHNE Sprach-Tag)
- ```text wird nur für Text-Prompts verwendet (wenn der Block mit ```text BEGINNT)

**Verwendung von ```text:**

Nur korrekt, wenn der gesamte Block ein Text-Prompt ist:

````markdown
```text
Erstelle ein Programm, das zwei Zahlen addiert.
```
````

**Bei automatischen Markdown-Korrekturen:**

- NIEMALS ```text als Code-Block-Ender hinzufügen
- Prüfe nach automatischen Linting-Fixes alle Code-Blöcke manuell
- Bei Unsicherheit: Code-Block-Ender ist IMMER nur ```

---

Letzte Aktualisierung: 2025-11-20
