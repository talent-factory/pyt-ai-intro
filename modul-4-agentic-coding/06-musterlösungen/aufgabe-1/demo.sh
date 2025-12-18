#!/bin/bash
# Demo-Skript für Task Manager CLI
# Zeigt alle Features des Tools

echo "🎯 Task Manager CLI - Demo"
echo "=========================="
echo ""

# Cleanup vorheriger Demo-Daten
rm -rf ~/.task_manager/demo_tasks.json 2>/dev/null

echo "📝 1. Tasks erstellen"
echo "--------------------"
uv run task add "Code reviewen" --priority high
uv run task add "Dokumentation schreiben" --priority medium
uv run task add "Tests erweitern" --priority low
uv run task add "Bug #123 fixen" --priority high
uv run task add "Meeting vorbereiten" --priority medium
echo ""

echo "📋 2. Alle Tasks auflisten"
echo "-------------------------"
uv run task list
echo ""

echo "✅ 3. Task erledigen"
echo "-------------------"
uv run task complete 1
uv run task complete 3
echo ""

echo "📋 4. Nur offene Tasks"
echo "---------------------"
uv run task list --status open
echo ""

echo "📋 5. Nur erledigte Tasks"
echo "------------------------"
uv run task list --status done
echo ""

echo "📊 6. Statistiken"
echo "----------------"
uv run task stats
echo ""

echo "🗑️  7. Task löschen"
echo "------------------"
echo "y" | uv run task delete 5
echo ""

echo "📋 8. Finale Task-Liste"
echo "----------------------"
uv run task list
echo ""

echo "✨ Demo abgeschlossen!"
echo ""
echo "💡 Weitere Commands:"
echo "   uv run task --help          - Hilfe anzeigen"
echo "   uv run task add --help      - Hilfe für 'add' Command"
echo "   uv run task list --help     - Hilfe für 'list' Command"
echo ""
echo "📁 Daten gespeichert in: ~/.task_manager/"
echo "   - tasks.json         - Task-Daten"
echo "   - task_manager.log   - Log-Datei"

