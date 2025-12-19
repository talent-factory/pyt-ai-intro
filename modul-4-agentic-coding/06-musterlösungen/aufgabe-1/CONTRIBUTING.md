# Contributing zu Task Manager CLI

Vielen Dank für dein Interesse, zu diesem Projekt beizutragen! 🎉

## 🚀 Schnellstart

1. **Repository forken**
   ```bash
   # Auf GitHub forken, dann:
   git clone https://github.com/DEIN-USERNAME/task-manager-cli.git
   cd task-manager-cli
   ```

2. **Development-Umgebung einrichten**
   ```bash
   # UV installieren (falls noch nicht vorhanden)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Dependencies installieren
   uv sync --all-extras
   ```

3. **Branch erstellen**
   ```bash
   git checkout -b feature/mein-feature
   ```

## 📋 Entwicklungs-Workflow

### 1. Code schreiben

- Folge den bestehenden Code-Konventionen
- Schreibe Type Hints für alle Funktionen
- Füge Docstrings hinzu (Google-Style)

### 2. Tests schreiben

```bash
# Neue Tests in tests/ erstellen
# Tests ausführen
uv run pytest

# Mit Coverage
uv run pytest --cov=task_manager
```

### 3. Code formatieren

```bash
# Automatisch formatieren
uv run black task_manager tests

# Linting
uv run flake8 task_manager tests

# Type Checking
uv run mypy task_manager
```

### 4. Alle Checks ausführen

```bash
# Mit Makefile
make all

# Oder manuell
uv run black task_manager tests
uv run flake8 task_manager tests
uv run mypy task_manager
uv run pytest --cov=task_manager
```

## 🎯 Code-Standards

### Python-Stil

- **Formatierung:** Black (line-length=100)
- **Linting:** Flake8
- **Type Checking:** Mypy
- **Docstrings:** Google-Style

### Beispiel

```python
def add_task(self, task: Task) -> None:
    """Fügt einen neuen Task hinzu.
    
    Args:
        task: Hinzuzufügender Task
        
    Raises:
        ValueError: Wenn Task ungültig ist
    """
    if not task.title:
        raise ValueError("Task muss einen Titel haben")
    
    tasks = self.load_tasks()
    tasks.append(task)
    self.save_tasks(tasks)
```

### Testing

- Mindestens 80% Coverage
- Fixtures für Setup/Teardown
- Aussagekräftige Test-Namen
- Arrange-Act-Assert Pattern

```python
def test_add_task(temp_storage):
    """Test: Task hinzufügen."""
    # Arrange
    task = Task(id=1, title="Test Task")
    
    # Act
    temp_storage.add_task(task)
    
    # Assert
    tasks = temp_storage.load_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"
```

## 🐛 Bug Reports

Beim Melden von Bugs bitte folgende Informationen angeben:

1. **Beschreibung:** Was ist das Problem?
2. **Reproduktion:** Schritte zum Reproduzieren
3. **Erwartetes Verhalten:** Was sollte passieren?
4. **Aktuelles Verhalten:** Was passiert tatsächlich?
5. **Umgebung:** OS, Python-Version, etc.

**Template:**

```markdown
## Bug-Beschreibung
[Kurze Beschreibung]

## Reproduktion
1. Schritt 1
2. Schritt 2
3. ...

## Erwartetes Verhalten
[Was sollte passieren]

## Aktuelles Verhalten
[Was passiert tatsächlich]

## Umgebung
- OS: [z.B. macOS 14.0]
- Python: [z.B. 3.11.5]
- Task Manager Version: [z.B. 1.0.0]
```

## 💡 Feature Requests

Feature-Vorschläge sind willkommen! Bitte beschreibe:

1. **Use Case:** Wofür wird das Feature benötigt?
2. **Vorschlag:** Wie könnte es implementiert werden?
3. **Alternativen:** Welche Alternativen gibt es?

## 📝 Pull Requests

### Vor dem PR

- [ ] Tests geschrieben und bestanden
- [ ] Code formatiert (black)
- [ ] Linting erfolgreich (flake8)
- [ ] Type Checking erfolgreich (mypy)
- [ ] Dokumentation aktualisiert
- [ ] CHANGELOG.md aktualisiert

### PR-Beschreibung

```markdown
## Änderungen
[Beschreibung der Änderungen]

## Motivation
[Warum ist diese Änderung notwendig?]

## Tests
[Welche Tests wurden hinzugefügt/geändert?]

## Checklist
- [ ] Tests bestanden
- [ ] Code formatiert
- [ ] Dokumentation aktualisiert
```

## 🔄 Review-Prozess

1. **Automatische Checks:** GitHub Actions muss erfolgreich sein
2. **Code Review:** Mindestens ein Maintainer muss approven
3. **Merge:** Nach Approval wird der PR gemerged

## 📚 Ressourcen

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [pytest Documentation](https://docs.pytest.org/)
- [Click Documentation](https://click.palletsprojects.com/)

## 🤝 Code of Conduct

- Sei respektvoll und konstruktiv
- Hilf anderen beim Lernen
- Akzeptiere konstruktive Kritik
- Fokussiere auf das Beste für das Projekt

## 📧 Kontakt

Bei Fragen kannst du:

- Ein Issue erstellen
- Eine Discussion starten
- Die Maintainer kontaktieren

Vielen Dank für deinen Beitrag! 🙏

