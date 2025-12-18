"""Tests für Storage-Layer."""

import pytest

from task_manager.models import Status, Task
from task_manager.storage import TaskStorage


@pytest.fixture
def temp_storage(tmp_path):
    """Erstellt temporären Storage für Tests.

    Args:
        tmp_path: Pytest-Fixture für temporäres Verzeichnis

    Yields:
        TaskStorage-Instanz mit temporärem Pfad
    """
    storage_path = tmp_path / "test_tasks.json"
    return TaskStorage(storage_path)


class TestTaskStorage:
    """Tests für TaskStorage-Klasse."""

    def test_storage_initialization(self, temp_storage):
        """Test: Storage wird korrekt initialisiert."""
        assert temp_storage.storage_path.exists()
        assert temp_storage.storage_path.read_text() == "[]"

    def test_add_task(self, temp_storage):
        """Test: Task hinzufügen."""
        task = Task(id=1, title="Test Task")
        temp_storage.add_task(task)

        tasks = temp_storage.load_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
        assert tasks[0].title == "Test Task"

    def test_load_tasks(self, temp_storage):
        """Test: Tasks laden."""
        task1 = Task(id=1, title="Task 1")
        task2 = Task(id=2, title="Task 2")

        temp_storage.add_task(task1)
        temp_storage.add_task(task2)

        tasks = temp_storage.load_tasks()
        assert len(tasks) == 2

    def test_get_task(self, temp_storage):
        """Test: Einzelnen Task abrufen."""
        task = Task(id=1, title="Test Task")
        temp_storage.add_task(task)

        retrieved = temp_storage.get_task(1)
        assert retrieved is not None
        assert retrieved.id == 1
        assert retrieved.title == "Test Task"

    def test_get_task_not_found(self, temp_storage):
        """Test: Nicht existierenden Task abrufen."""
        result = temp_storage.get_task(999)
        assert result is None

    def test_update_task(self, temp_storage):
        """Test: Task aktualisieren."""
        task = Task(id=1, title="Original Title")
        temp_storage.add_task(task)

        task.title = "Updated Title"
        task.complete()
        success = temp_storage.update_task(task)

        assert success is True

        updated = temp_storage.get_task(1)
        assert updated.title == "Updated Title"
        assert updated.status == Status.DONE

    def test_update_task_not_found(self, temp_storage):
        """Test: Nicht existierenden Task aktualisieren."""
        task = Task(id=999, title="Non-existent")
        success = temp_storage.update_task(task)

        assert success is False

    def test_delete_task(self, temp_storage):
        """Test: Task löschen."""
        task = Task(id=1, title="Test Task")
        temp_storage.add_task(task)

        success = temp_storage.delete_task(1)
        assert success is True

        tasks = temp_storage.load_tasks()
        assert len(tasks) == 0

    def test_delete_task_not_found(self, temp_storage):
        """Test: Nicht existierenden Task löschen."""
        success = temp_storage.delete_task(999)
        assert success is False

    def test_get_next_id_empty(self, temp_storage):
        """Test: Nächste ID bei leerem Storage."""
        next_id = temp_storage.get_next_id()
        assert next_id == 1

    def test_get_next_id_with_tasks(self, temp_storage):
        """Test: Nächste ID mit existierenden Tasks."""
        temp_storage.add_task(Task(id=1, title="Task 1"))
        temp_storage.add_task(Task(id=2, title="Task 2"))

        next_id = temp_storage.get_next_id()
        assert next_id == 3

    def test_filter_tasks_all(self, temp_storage):
        """Test: Alle Tasks filtern."""
        temp_storage.add_task(Task(id=1, title="Task 1"))
        temp_storage.add_task(Task(id=2, title="Task 2"))

        tasks = temp_storage.filter_tasks()
        assert len(tasks) == 2

    def test_filter_tasks_by_status(self, temp_storage):
        """Test: Tasks nach Status filtern."""
        task1 = Task(id=1, title="Open Task")
        task2 = Task(id=2, title="Done Task")
        task2.complete()

        temp_storage.add_task(task1)
        temp_storage.add_task(task2)

        open_tasks = temp_storage.filter_tasks(Status.OPEN)
        done_tasks = temp_storage.filter_tasks(Status.DONE)

        assert len(open_tasks) == 1
        assert len(done_tasks) == 1
        assert open_tasks[0].title == "Open Task"
        assert done_tasks[0].title == "Done Task"

    def test_invalid_json_handling(self, temp_storage):
        """Test: Fehlerbehandlung bei ungültigem JSON."""
        temp_storage.storage_path.write_text("invalid json")

        with pytest.raises(ValueError, match="Ungültiges JSON-Format"):
            temp_storage.load_tasks()

    def test_persistence(self, temp_storage):
        """Test: Daten bleiben nach Neuinitialisierung erhalten."""
        task = Task(id=1, title="Persistent Task")
        temp_storage.add_task(task)

        # Neuen Storage mit gleichem Pfad erstellen
        new_storage = TaskStorage(temp_storage.storage_path)
        tasks = new_storage.load_tasks()

        assert len(tasks) == 1
        assert tasks[0].title == "Persistent Task"
