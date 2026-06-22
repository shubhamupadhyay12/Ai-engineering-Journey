from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.tools import tool
import requests
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke('top news in india today')

model = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
llm = ChatHuggingFace(llm=model)


from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull(
    "hwchase17/react",
    dangerously_pull_public_prompt=True
)  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})
# print(response)            

print(response['output'])

#u can ceate a another tool of weather