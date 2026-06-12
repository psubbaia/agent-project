from planner import create_plan
from tools import add_task, list_tasks


def main():

    goal = input("Enter your goal: ")

    plan = create_plan(goal)

    print("\nGenerated Plan:")

    for step in plan:
        print("-", step)
        add_task(step)

    print("\nTasks saved:\n")

    for task in list_tasks():
        print(
            f"[{task['id']}] "
            f"{task['title']} "
            f"({task['status']})"
        )


if __name__ == "__main__":
    main()