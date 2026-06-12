from planner import create_plan
from tools import add_task, list_tasks
from memory import load_state, save_state


def main():
    state = load_state()

    goal = input("Enter your goal: ")

    plan = create_plan(goal)

    state["current_goal"] = goal
    state["current_plan"] = plan
    state["completed_tasks"] = []

    save_state(state)

    print("\nGenerated Plan:\n")

    for step in plan:
        print("-", step)
        add_task(step)

    print("\nTasks saved:\n")

    for task in list_tasks():
        print(f"[{task['id']}] {task['title']} ({task['status']})")


if __name__ == "__main__":
    main()