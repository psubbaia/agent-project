from mcp.client import use_tool


def get_next_task():
    return use_tool("get_next_task")


def get_knowledge_for_goal():
    from memory import load_state

    state = load_state()
    goal = state.get("current_goal", "")

    if not goal:
        return []

    return use_tool("search_documents", goal)