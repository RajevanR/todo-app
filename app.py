def add_task(tasks, title):
    """Ajoute une tâche à la liste."""
    return list(tasks) + [title]

def count_tasks(tasks):
    return len(tasks)

if __name__ == "__main__":
    items = []
    items = add_task(items, "Première tâche")
    print(f"Nombre de tâches: {count_tasks(items)}")
