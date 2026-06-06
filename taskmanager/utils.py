# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status   = "[x]" if task["done"] else "[ ]"
    priority = task.get("priority", "normal")
    title    = (task.get("title") or "Sem título").upper()
    return f"{status} [{priority}] #{task['id']} - {title}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        pending = [t for t in tasks if not t["done"]]
        done    = [t for t in tasks if t["done"]]
        return pending + done
    return [t for t in tasks if not t["done"]]
