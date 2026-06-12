from planner import create_plan
from tools import add_task, list_tasks, clear_tasks
from memory import load_state, save_state
from agent import get_next_task, get_knowledge_for_goal


def main():
    state = load_state()

    goal = input("Enter your goal: ").strip()

    if not goal:
        print("No goal entered.")
        return

    current_goal = state.get("current_goal", "")

    if goal != current_goal:
        clear_tasks()

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
    else:
        print("\nGoal already exists. Using saved plan.\n")

    print("\nKnowledge Retrieval:\n")
    knowledge = get_knowledge_for_goal()

    if knowledge:
        for doc in knowledge:
            print(f"From {doc['filename']}:")
            print(doc["content"])
            print()
    else:
        print("No relevant documents found.")

    print("\nCurrent Tasks:\n")
    for task in list_tasks():
        print(f"[{task['id']}] {task['title']} ({task['status']})")

    next_task = get_next_task()

    print("\nAgent Recommendation:")
    if next_task:
        print(f"Next Task: {next_task['title']}")
    else:
        print("All tasks completed!")


if __name__ == "__main__":
    main()