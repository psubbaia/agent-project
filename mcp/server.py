from tools import list_tasks
from rag.retrieve import search_documents
from agent import get_next_task


TOOLS = {
    "list_tasks": list_tasks,
    "search_documents": search_documents,
    "get_next_task": get_next_task
}


def list_tools():
    return list(TOOLS.keys())


def call_tool(tool_name, *args):
    if tool_name not in TOOLS:
        raise ValueError(f"Unknown tool: {tool_name}")

    return TOOLS[tool_name](*args)