from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from pydantic import BaseModel , Field
from typing import Literal 
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from langchain_core.runnables import RunnableBranch , RunnableLambda



load_dotenv()
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

class feedback(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description='give the sentiment of the feedback')
    
parser2 = PydanticOutputParser(pydantic_object=feedback)


prompt1 = PromptTemplate(
    template =  "classify the sentiment of the following feedback into positive, negative  \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

brach_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt3 | model | parser),
    RunnableLambda(lambda x:'could not find sentiment')
)

chain = classifier_chain | brach_chain

print(chain.invoke({'feedback':'this is a terrible phone'}))

chain.get_graph().print_ascii()