from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import requests

#tool create 

@tool
def multiply(a:int,b:int) -> int:
    """given two number a and b this tool returns their product"""
    return a*b


# print(multiply.invoke({"a":3,"b":4}))


#tool binding

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

model_with_tool = model.bind_tools([multiply])  #this is tool binding, oly few llm allows tool binding



#tool execution

# print(multiply.invoke(result.tool_calls[0]))

query = HumanMessage("can you multiply 3 wiht 1000 ")

messages = [query]
result = model_with_tool.invoke(messages)
messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

# print(messages)

print(model_with_tool.invoke(messages).content)