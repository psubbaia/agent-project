def create_plan(goal):
    """
    Convert a user goal into a simple plan.
    """

    return [
        f"Understand {goal}",
        f"Research {goal}",
        f"Create action items for {goal}",
        f"Execute tasks for {goal}",
        "Review progress"
    ]