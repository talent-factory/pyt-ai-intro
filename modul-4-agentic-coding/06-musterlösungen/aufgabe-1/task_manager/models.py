"""Datenmodelle für den Task Manager."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Priority(str, Enum):
    """Task-Priorität."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(str, Enum):
    """Task-Status."""

    OPEN = "open"
    DONE = "done"


@dataclass
class Task:
    """Repräsentiert eine einzelne Aufgabe.

    Attributes:
        id: Eindeutige Task-ID
        title: Titel der Aufgabe
        priority: Priorität (low, medium, high)
        status: Status (open, done)
        created_at: Erstellungszeitpunkt
        completed_at: Abschlusszeitpunkt (optional)
    """

    id: int
    title: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.OPEN
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        """Konvertiert Task zu Dictionary für JSON-Serialisierung.

        Returns:
            Dictionary-Repräsentation des Tasks
        """
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Erstellt Task aus Dictionary.

        Args:
            data: Dictionary mit Task-Daten

        Returns:
            Task-Instanz
        """
        return cls(
            id=data["id"],
            title=data["title"],
            priority=Priority(data["priority"]),
            status=Status(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            completed_at=(
                datetime.fromisoformat(data["completed_at"]) if data.get("completed_at") else None
            ),
        )

    def complete(self) -> None:
        """Markiert Task als erledigt."""
        self.status = Status.DONE
        self.completed_at = datetime.now()

    def __str__(self) -> str:
        """String-Repräsentation des Tasks.

        Returns:
            Formatierter Task-String
        """
        status_icon = "✓" if self.status == Status.DONE else "○"
        priority_icon = {
            Priority.LOW: "🔵",
            Priority.MEDIUM: "🟡",
            Priority.HIGH: "🔴",
        }[self.priority]

        return f"{status_icon} [{self.id}] {priority_icon} {self.title}"
