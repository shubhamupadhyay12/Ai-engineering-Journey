from langchain_core.tools import tool
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests 
from langchain_core.tools import InjectedToolArg
from typing import Annotated


#tool create

@tool
def get_conversion_factor(base_currency : str ,target_currency: str ) -> float:
    """this function fetches the currency convertion factor between a given base currency and a target currency"""
    url = f'https://v6.exchangerate-api.com/v6/bfa6fe92a5a97a9e65ab14c6/pair/{base_currency}/{target_currency}'
    
    response = requests.get(url)
    return response.json()


@tool
def convert(base_currency : int , conversion_rate:Annotated[float,InjectedToolArg])->float:
    '''given a currency convertion rate this function calculates the target currency value from a given base currency value'''
    return base_currency*conversion_rate



#tool binding

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

model_with_tool = model.bind_tools([convert,get_conversion_factor])

messages = [HumanMessage('what is the convertion factor between USD and INR and based on that can you convert 10 usd to inr ')]

ai_message = model_with_tool.invoke(messages)

messages.append(ai_message)


import json
for tool_call in ai_message.tool_calls:
    #execute the 1sst tool and get the value of convertion rate 
    if tool_call['name']== 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
        #fetch this convertion rate
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        #appendd this tool message to message list
        messages.append(tool_message1)
    #execute the 2nd tool using the conversion rate from tool 1
    if tool_call['name']=='convert':
        #fetch the current arg
        tool_call['args']['conversion_rate']=conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)
        
print(model_with_tool.invoke(messages).content)

