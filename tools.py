import json
import os

TASKS_FILE = os.path.join("data", "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, priority="medium"):
    tasks = load_tasks()
    new_id = 1 if not tasks else max(task["id"] for task in tasks) + 1
    task = {
        "id": new_id,
        "title": title,
        "status": "pending",
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks():
    return load_tasks()


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            return task
    return None