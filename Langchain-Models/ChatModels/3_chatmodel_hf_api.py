from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a five line poem on Cricket")
print(result.content)