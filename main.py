from planner import create_plan
from tools import add_task, list_tasks
from memory import load_state, save_state
from agent import get_next_action, mark_next_task_done


def main():
    state = load_state()

    if not state.get("current_goal"):
        goal = input("Enter your goal: ")
        plan = create_plan(goal)

        state["current_goal"] = goal
        state["current_plan"] = plan
        state["completed_tasks"] = []
        save_state(state)

        for step in plan:
            add_task(step)

        print("\nGenerated Plan:\n")
        for step in plan:
            print("-", step)

    print("\nCurrent Tasks:\n")
    for task in list_tasks():
        print(f"[{task['id']}] {task['title']} ({task['status']})")

    print("\nAgent Decision:")
    print(get_next_action())

    choice = input("\nMark next task done? (y/n): ").lower()

    if choice == "y":
        result = mark_next_task_done()
        print(result)

    print("\nUpdated Tasks:\n")
    for task in list_tasks():
        print(f"[{task['id']}] {task['title']} ({task['status']})")


if __name__ == "__main__":
    main()