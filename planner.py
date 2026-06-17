from llm_planner import create_plan_with_llm


def create_plan(goal):
    try:
        return create_plan_with_llm(goal)
    except Exception as error:
        print(f"LLM planner failed. Using fallback planner. Error: {error}")

        goal = goal.strip()
        return [
            f"Understand {goal}",
            f"Research {goal}",
            f"Create action items for {goal}",
            f"Execute tasks for {goal}",
            "Review progress"
        ]