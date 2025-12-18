"""Tests für CLI-Commands."""

import pytest
from click.testing import CliRunner
from task_manager.cli import cli
from task_manager.storage import TaskStorage


@pytest.fixture
def runner():
    """Erstellt Click CLI Runner.

    Yields:
        CliRunner-Instanz
    """
    return CliRunner()


@pytest.fixture
def temp_storage_path(tmp_path):
    """Erstellt temporären Storage-Pfad.

    Args:
        tmp_path: Pytest-Fixture für temporäres Verzeichnis

    Yields:
        Pfad zur temporären Storage-Datei
    """
    return tmp_path / "test_tasks.json"


class TestCLI:
    """Tests für CLI-Commands."""

    def test_cli_help(self, runner):
        """Test: CLI Help-Text."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Task Manager" in result.output

    def test_cli_version(self, runner):
        """Test: CLI Version."""
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "1.0.0" in result.output


class TestAddCommand:
    """Tests für 'add' Command."""

    def test_add_task_default_priority(self, runner, temp_storage_path, monkeypatch):
        """Test: Task mit Standard-Priorität hinzufügen."""
        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["add", "Test Task"])
        assert result.exit_code == 0
        assert "Task hinzugefügt" in result.output

        storage = TaskStorage(temp_storage_path)
        tasks = storage.load_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test Task"

    def test_add_task_with_priority(self, runner, temp_storage_path, monkeypatch):
        """Test: Task mit spezifischer Priorität hinzufügen."""
        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["add", "Urgent Task", "--priority", "high"])
        assert result.exit_code == 0

        storage = TaskStorage(temp_storage_path)
        tasks = storage.load_tasks()
        assert tasks[0].priority.value == "high"


class TestListCommand:
    """Tests für 'list' Command."""

    def test_list_empty(self, runner, temp_storage_path, monkeypatch):
        """Test: Leere Task-Liste."""
        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        assert "Keine Tasks gefunden" in result.output

    def test_list_all_tasks(self, runner, temp_storage_path, monkeypatch):
        """Test: Alle Tasks auflisten."""
        storage = TaskStorage(temp_storage_path)
        from task_manager.models import Task

        storage.add_task(Task(id=1, title="Task 1"))
        storage.add_task(Task(id=2, title="Task 2"))

        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        assert "Task 1" in result.output
        assert "Task 2" in result.output

    def test_list_filter_open(self, runner, temp_storage_path, monkeypatch):
        """Test: Nur offene Tasks auflisten."""
        storage = TaskStorage(temp_storage_path)
        from task_manager.models import Task

        task1 = Task(id=1, title="Open Task")
        task2 = Task(id=2, title="Done Task")
        task2.complete()

        storage.add_task(task1)
        storage.add_task(task2)

        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["list", "--status", "open"])
        assert result.exit_code == 0
        assert "Open Task" in result.output
        assert "Done Task" not in result.output


class TestCompleteCommand:
    """Tests für 'complete' Command."""

    def test_complete_task(self, runner, temp_storage_path, monkeypatch):
        """Test: Task als erledigt markieren."""
        storage = TaskStorage(temp_storage_path)
        from task_manager.models import Task

        storage.add_task(Task(id=1, title="Test Task"))

        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["complete", "1"])
        assert result.exit_code == 0
        assert "erledigt markiert" in result.output

        task = storage.get_task(1)
        assert task.status.value == "done"

    def test_complete_nonexistent_task(self, runner, temp_storage_path, monkeypatch):
        """Test: Nicht existierenden Task erledigen."""
        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["complete", "999"])
        assert result.exit_code == 1
        assert "nicht gefunden" in result.output


class TestDeleteCommand:
    """Tests für 'delete' Command."""

    def test_delete_task(self, runner, temp_storage_path, monkeypatch):
        """Test: Task löschen."""
        storage = TaskStorage(temp_storage_path)
        from task_manager.models import Task

        storage.add_task(Task(id=1, title="Test Task"))

        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["delete", "1"], input="y\n")
        assert result.exit_code == 0
        assert "gelöscht" in result.output

        assert storage.get_task(1) is None


class TestStatsCommand:
    """Tests für 'stats' Command."""

    def test_stats_empty(self, runner, temp_storage_path, monkeypatch):
        """Test: Statistiken bei leerer Liste."""
        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["stats"])
        assert result.exit_code == 0
        assert "Keine Tasks vorhanden" in result.output

    def test_stats_with_tasks(self, runner, temp_storage_path, monkeypatch):
        """Test: Statistiken mit Tasks."""
        storage = TaskStorage(temp_storage_path)
        from task_manager.models import Priority, Task

        task1 = Task(id=1, title="Task 1", priority=Priority.HIGH)
        task2 = Task(id=2, title="Task 2")
        task2.complete()

        storage.add_task(task1)
        storage.add_task(task2)

        monkeypatch.setattr(
            "task_manager.cli.TaskStorage", lambda: TaskStorage(temp_storage_path)
        )

        result = runner.invoke(cli, ["stats"])
        assert result.exit_code == 0
        assert "Gesamt:" in result.output
        assert "Offen:" in result.output
        assert "Erledigt:" in result.output
        assert "Abschlussrate:" in result.output
