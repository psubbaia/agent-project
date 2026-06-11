from tools import add_task, list_tasks, complete_task


def main():
    print("Testing task manager...")

    add_task("Research company")
    add_task("Review resume")
    add_task("Practice interview questions")

    print("Current tasks:")
    for task in list_tasks():
        print(task)

    complete_task(1)

    print("\nAfter completing task 1:")
    for task in list_tasks():
        print(task)


if __name__ == "__main__":
    main()