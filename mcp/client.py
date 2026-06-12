from mcp.server import list_tools, call_tool


def discover_tools():
    return list_tools()


def use_tool(tool_name, *args):
    return call_tool(tool_name, *args)