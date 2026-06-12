from memory import load_state, save_state
from tools import list_tasks, complete_task


def get_next_action():
    state = load_state()
    plan = state.get("current_plan", [])

    tasks = list_tasks()

    pending_tasks = [task for task in tasks if task["status"] != "done"]

    if not state.get("current_goal"):
        return "No goal found. Please enter a goal first."

    if not pending_tasks:
        return "All tasks are complete."

    next_task = pending_tasks[0]
    return f"Next task: {next_task['title']}"


def mark_next_task_done():
    tasks = list_tasks()

    for task in tasks:
        if task["status"] != "done":
            complete_task(task["id"])
            return f"Completed task: {task['title']}"

    return "No pending tasks found."


def run_agent():
    state = load_state()

    if not state.get("current_goal"):
        goal = input("Enter your goal: ")
        state["current_goal"] = goal
        save_state(state)

    print(get_next_action())