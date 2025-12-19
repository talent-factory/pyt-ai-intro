"""Tests für Task-Modelle."""

from datetime import datetime

from task_manager.models import Priority, Status, Task


class TestTask:
    """Tests für die Task-Klasse."""

    def test_task_creation(self):
        """Test: Task wird korrekt erstellt."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.priority == Priority.MEDIUM
        assert task.status == Status.OPEN
        assert task.completed_at is None
        assert isinstance(task.created_at, datetime)

    def test_task_with_priority(self):
        """Test: Task mit spezifischer Priorität."""
        task = Task(id=1, title="Urgent Task", priority=Priority.HIGH)

        assert task.priority == Priority.HIGH

    def test_task_complete(self):
        """Test: Task als erledigt markieren."""
        task = Task(id=1, title="Test Task")

        assert task.status == Status.OPEN
        assert task.completed_at is None

        task.complete()

        assert task.status == Status.DONE
        assert task.completed_at is not None
        assert isinstance(task.completed_at, datetime)

    def test_task_to_dict(self):
        """Test: Task zu Dictionary konvertieren."""
        task = Task(id=1, title="Test Task", priority=Priority.HIGH)
        data = task.to_dict()

        assert data["id"] == 1
        assert data["title"] == "Test Task"
        assert data["priority"] == "high"
        assert data["status"] == "open"
        assert "created_at" in data
        assert data["completed_at"] is None

    def test_task_from_dict(self):
        """Test: Task aus Dictionary erstellen."""
        data = {
            "id": 1,
            "title": "Test Task",
            "priority": "high",
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
        }

        task = Task.from_dict(data)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.priority == Priority.HIGH
        assert task.status == Status.OPEN

    def test_task_roundtrip(self):
        """Test: Task -> Dict -> Task bleibt gleich."""
        original = Task(id=1, title="Test Task", priority=Priority.LOW)
        data = original.to_dict()
        restored = Task.from_dict(data)

        assert restored.id == original.id
        assert restored.title == original.title
        assert restored.priority == original.priority
        assert restored.status == original.status

    def test_task_str_representation(self):
        """Test: String-Repräsentation des Tasks."""
        task = Task(id=1, title="Test Task", priority=Priority.HIGH)
        task_str = str(task)

        assert "1" in task_str
        assert "Test Task" in task_str
        assert "🔴" in task_str  # High priority icon
        assert "○" in task_str  # Open status icon

    def test_task_str_representation_completed(self):
        """Test: String-Repräsentation eines erledigten Tasks."""
        task = Task(id=1, title="Test Task")
        task.complete()
        task_str = str(task)

        assert "✓" in task_str  # Done status icon


class TestPriority:
    """Tests für Priority Enum."""

    def test_priority_values(self):
        """Test: Priority-Werte sind korrekt."""
        assert Priority.LOW.value == "low"
        assert Priority.MEDIUM.value == "medium"
        assert Priority.HIGH.value == "high"

    def test_priority_from_string(self):
        """Test: Priority aus String erstellen."""
        assert Priority("low") == Priority.LOW
        assert Priority("medium") == Priority.MEDIUM
        assert Priority("high") == Priority.HIGH


class TestStatus:
    """Tests für Status Enum."""

    def test_status_values(self):
        """Test: Status-Werte sind korrekt."""
        assert Status.OPEN.value == "open"
        assert Status.DONE.value == "done"

    def test_status_from_string(self):
        """Test: Status aus String erstellen."""
        assert Status("open") == Status.OPEN
        assert Status("done") == Status.DONE
