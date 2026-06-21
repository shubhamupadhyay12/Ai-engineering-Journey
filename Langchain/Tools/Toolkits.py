'''Just a collecetion of related tools that serve a common purpose
packages together for convenience and reusability

   A toolkit is just a collection (bundle) of related tools that serve a common purpose packaged together for convenience and reusability.
In LangChain:
. A toolkit might be: Google Drive ToolKit
. And it can contain the following tools


GoogleDriveCreateFileTool: Upload a file
GoogleDriveSearch Tool: Search for a file by name/content
GoogleDriveReadFileTool: Read contents of a file    '''

from langchain_core.tools import tool

# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)
