"""Command-Line Interface für den Task Manager."""

import logging
import sys
from pathlib import Path
from typing import Optional

import click

from .models import Priority, Status, Task
from .storage import TaskStorage

# Logging konfigurieren
log_dir = Path.home() / ".task_manager"
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "task_manager.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Task Manager - Verwalte deine Aufgaben effizient."""
    pass


@cli.command()
@click.argument("title")
@click.option(
    "--priority",
    "-p",
    type=click.Choice(["low", "medium", "high"], case_sensitive=False),
    default="medium",
    help="Priorität der Aufgabe",
)
def add(title: str, priority: str) -> None:
    """Fügt eine neue Aufgabe hinzu.

    Args:
        title: Titel der Aufgabe
        priority: Priorität (low, medium, high)
    """
    try:
        storage = TaskStorage()
        task = Task(
            id=storage.get_next_id(),
            title=title,
            priority=Priority(priority.lower()),
        )
        storage.add_task(task)
        click.echo(click.style(f"✓ Task hinzugefügt: {task}", fg="green"))
        logger.info(f"Task erstellt: {task.id} - {task.title}")
    except Exception as e:
        click.echo(click.style(f"✗ Fehler: {e}", fg="red"), err=True)
        logger.error(f"Fehler beim Hinzufügen: {e}")
        sys.exit(1)


@cli.command()
@click.option(
    "--status",
    "-s",
    type=click.Choice(["open", "done", "all"], case_sensitive=False),
    default="all",
    help="Filtere nach Status",
)
def list(status: str) -> None:
    """Listet alle Aufgaben auf.

    Args:
        status: Filter nach Status (open, done, all)
    """
    try:
        storage = TaskStorage()

        if status == "all":
            tasks = storage.filter_tasks()
        else:
            tasks = storage.filter_tasks(Status(status.lower()))

        if not tasks:
            click.echo(click.style("Keine Tasks gefunden.", fg="yellow"))
            return

        click.echo(click.style(f"\n📋 Tasks ({len(tasks)}):", fg="blue", bold=True))
        click.echo()

        for task in sorted(tasks, key=lambda t: t.id):
            color = "green" if task.status == Status.DONE else "white"
            click.echo(click.style(f"  {task}", fg=color))

        click.echo()
        logger.info(f"Tasks aufgelistet: {len(tasks)} Tasks")
    except Exception as e:
        click.echo(click.style(f"✗ Fehler: {e}", fg="red"), err=True)
        logger.error(f"Fehler beim Auflisten: {e}")
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
def complete(task_id: int) -> None:
    """Markiert eine Aufgabe als erledigt.

    Args:
        task_id: ID der zu erledigenden Aufgabe
    """
    try:
        storage = TaskStorage()
        task = storage.get_task(task_id)

        if not task:
            click.echo(click.style(f"✗ Task {task_id} nicht gefunden.", fg="red"), err=True)
            sys.exit(1)

        if task.status == Status.DONE:
            click.echo(click.style(f"ℹ Task {task_id} ist bereits erledigt.", fg="yellow"))
            return

        task.complete()
        storage.update_task(task)
        click.echo(click.style(f"✓ Task {task_id} als erledigt markiert.", fg="green"))
        logger.info(f"Task erledigt: {task_id}")
    except Exception as e:
        click.echo(click.style(f"✗ Fehler: {e}", fg="red"), err=True)
        logger.error(f"Fehler beim Abschliessen: {e}")
        sys.exit(1)


@cli.command()
@click.argument("task_id", type=int)
@click.confirmation_option(prompt="Möchtest du diesen Task wirklich löschen?")
def delete(task_id: int) -> None:
    """Löscht eine Aufgabe.

    Args:
        task_id: ID der zu löschenden Aufgabe
    """
    try:
        storage = TaskStorage()

        if storage.delete_task(task_id):
            click.echo(click.style(f"✓ Task {task_id} gelöscht.", fg="green"))
            logger.info(f"Task gelöscht: {task_id}")
        else:
            click.echo(click.style(f"✗ Task {task_id} nicht gefunden.", fg="red"), err=True)
            sys.exit(1)
    except Exception as e:
        click.echo(click.style(f"✗ Fehler: {e}", fg="red"), err=True)
        logger.error(f"Fehler beim Löschen: {e}")
        sys.exit(1)


@cli.command()
def stats() -> None:
    """Zeigt Statistiken über alle Aufgaben."""
    try:
        storage = TaskStorage()
        all_tasks = storage.load_tasks()

        if not all_tasks:
            click.echo(click.style("Keine Tasks vorhanden.", fg="yellow"))
            return

        open_tasks = [t for t in all_tasks if t.status == Status.OPEN]
        done_tasks = [t for t in all_tasks if t.status == Status.DONE]

        high_priority = len([t for t in open_tasks if t.priority == Priority.HIGH])
        medium_priority = len([t for t in open_tasks if t.priority == Priority.MEDIUM])
        low_priority = len([t for t in open_tasks if t.priority == Priority.LOW])

        completion_rate = (len(done_tasks) / len(all_tasks)) * 100 if all_tasks else 0

        click.echo(click.style("\n📊 Task-Statistiken:", fg="blue", bold=True))
        click.echo()
        click.echo(f"  Gesamt:           {len(all_tasks)}")
        click.echo(click.style(f"  Offen:            {len(open_tasks)}", fg="yellow"))
        click.echo(click.style(f"  Erledigt:         {len(done_tasks)}", fg="green"))
        click.echo(f"  Abschlussrate:    {completion_rate:.1f}%")
        click.echo()
        click.echo(click.style("  Offene Tasks nach Priorität:", fg="blue"))
        click.echo(click.style(f"    🔴 Hoch:        {high_priority}", fg="red"))
        click.echo(click.style(f"    🟡 Mittel:      {medium_priority}", fg="yellow"))
        click.echo(click.style(f"    🔵 Niedrig:     {low_priority}", fg="blue"))
        click.echo()

        logger.info("Statistiken angezeigt")
    except Exception as e:
        click.echo(click.style(f"✗ Fehler: {e}", fg="red"), err=True)
        logger.error(f"Fehler bei Statistiken: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli()
