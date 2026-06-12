from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables=['topic']
)

prompt2  = PromptTemplate(
    template = 'explain the joke \n {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "summary":RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = chain.invoke({'topic':"sex"})
print(result)
chain.get_graph().print_ascii()