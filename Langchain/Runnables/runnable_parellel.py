from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro")
model = ChatHuggingFace(llm=llm)


parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = 'generate a linkedin post about {topic}',
    input_variables=['topic']
)

parellel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'post':RunnableSequence(prompt2,model,parser)
})

print(parellel_chain.invoke({'topic':'AI'}))