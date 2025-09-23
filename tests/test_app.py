from app import add_task, count_tasks

def test_add_and_count():
    items = []
    items2 = add_task(items, "A")
    assert items == []     # la liste d'origine reste inchangée
    assert count_tasks(items2) == 1
    items3 = add_task(items2, "B")
    assert count_tasks(items3) == 2
