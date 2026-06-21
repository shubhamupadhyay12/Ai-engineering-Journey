from langchain_core.tools import tool

#step 1 create  a function 

def multiply(a,b):
    '''Multiply two number'''  #docshinting
    return a*b


# Step 2 - add type hints

def multiply(a: int, b:int) -> int: 
    """Multiply two numbers"""
    return a*b

# Step 3 - add tool decorator

@tool  #just a decorator to make a tool 
def multiply(a: int, b:int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":2,"b":4})

print(multiply.name)
print(multiply.description)
print(multiply.args)


















# 2nd method to cerate a tool using structuredtool and pydantic

from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")

def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':3, 'b':3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)






















# 3rd method to create a tool by using BaseTool

from langchain.tools import BaseTool
from typing import Type

# arg schema using pydantic

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to add")
    b: int = Field(required=True, description="The second number to add")
    
    
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:   #u can write only run 
        return a * b
    
multiply_tool = MultiplyTool()
    
result = multiply_tool.invoke({'a':3, 'b':3})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)

print(multiply_tool.args)