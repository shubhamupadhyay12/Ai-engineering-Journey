from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnableLambda , RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

#creating a runnable
def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

prompt = PromptTemplate(
    template = "Tell me one joke about {topic}",
    input_variables=['topic']
)

get_joke = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'number_of_words': runnable_word_counter
})

main_chain = RunnableSequence(get_joke,parallel_chain)

result = main_chain.invoke({'topic':'sex'})
print(result)