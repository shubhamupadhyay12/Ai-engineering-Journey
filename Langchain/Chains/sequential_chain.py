from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro")
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = "generate detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "extract 5  most important points from {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':"cricekt"})

print(result)

chain.get_graph().print_ascii()