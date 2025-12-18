"""Storage-Layer für Task-Persistierung."""

import json
import logging
from pathlib import Path
from typing import List, Optional

from .models import Task, Status

logger = logging.getLogger(__name__)


class TaskStorage:
    """Verwaltet die Persistierung von Tasks in JSON-Dateien.

    Attributes:
        storage_path: Pfad zur JSON-Datei
    """

    def __init__(self, storage_path: Path = Path.home() / ".task_manager" / "tasks.json"):
        """Initialisiert den Storage.

        Args:
            storage_path: Pfad zur Storage-Datei
        """
        self.storage_path = storage_path
        self._ensure_storage_exists()
        logger.info(f"Storage initialisiert: {self.storage_path}")

    def _ensure_storage_exists(self) -> None:
        """Stellt sicher, dass Storage-Verzeichnis und -Datei existieren."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.exists():
            self.storage_path.write_text("[]")
            logger.debug("Neue Storage-Datei erstellt")

    def load_tasks(self) -> List[Task]:
        """Lädt alle Tasks aus der Storage-Datei.

        Returns:
            Liste aller Tasks

        Raises:
            ValueError: Bei ungültigem JSON-Format
        """
        try:
            data = json.loads(self.storage_path.read_text())
            tasks = [Task.from_dict(task_data) for task_data in data]
            logger.debug(f"{len(tasks)} Tasks geladen")
            return tasks
        except json.JSONDecodeError as e:
            logger.error(f"Fehler beim Laden der Tasks: {e}")
            raise ValueError(f"Ungültiges JSON-Format in {self.storage_path}") from e

    def save_tasks(self, tasks: List[Task]) -> None:
        """Speichert alle Tasks in die Storage-Datei.

        Args:
            tasks: Liste der zu speichernden Tasks
        """
        data = [task.to_dict() for task in tasks]
        self.storage_path.write_text(json.dumps(data, indent=2))
        logger.debug(f"{len(tasks)} Tasks gespeichert")

    def add_task(self, task: Task) -> None:
        """Fügt einen neuen Task hinzu.

        Args:
            task: Hinzuzufügender Task
        """
        tasks = self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)
        logger.info(f"Task hinzugefügt: {task.title}")

    def get_task(self, task_id: int) -> Optional[Task]:
        """Sucht einen Task anhand der ID.

        Args:
            task_id: ID des gesuchten Tasks

        Returns:
            Task oder None, falls nicht gefunden
        """
        tasks = self.load_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task: Task) -> bool:
        """Aktualisiert einen existierenden Task.

        Args:
            task: Zu aktualisierender Task

        Returns:
            True bei Erfolg, False wenn Task nicht gefunden
        """
        tasks = self.load_tasks()
        for i, t in enumerate(tasks):
            if t.id == task.id:
                tasks[i] = task
                self.save_tasks(tasks)
                logger.info(f"Task aktualisiert: {task.id}")
                return True
        logger.warning(f"Task nicht gefunden: {task.id}")
        return False

    def delete_task(self, task_id: int) -> bool:
        """Löscht einen Task.

        Args:
            task_id: ID des zu löschenden Tasks

        Returns:
            True bei Erfolg, False wenn Task nicht gefunden
        """
        tasks = self.load_tasks()
        initial_count = len(tasks)
        tasks = [t for t in tasks if t.id != task_id]

        if len(tasks) < initial_count:
            self.save_tasks(tasks)
            logger.info(f"Task gelöscht: {task_id}")
            return True

        logger.warning(f"Task nicht gefunden: {task_id}")
        return False

    def get_next_id(self) -> int:
        """Ermittelt die nächste verfügbare Task-ID.

        Returns:
            Nächste freie ID
        """
        tasks = self.load_tasks()
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1

    def filter_tasks(self, status: Optional[Status] = None) -> List[Task]:
        """Filtert Tasks nach Status.

        Args:
            status: Gewünschter Status (None = alle)

        Returns:
            Gefilterte Task-Liste
        """
        tasks = self.load_tasks()
        if status is None:
            return tasks
        return [task for task in tasks if task.status == status]
