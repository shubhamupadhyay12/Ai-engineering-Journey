from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro")
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = 'write one joke about an {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "explain the following joke {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1 , model , parser, prompt2 , model , parser)
result = chain.invoke({'topic':'AI'})
print(result)