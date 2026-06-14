from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "answer the following qustion- \n {question} from the following text - \n {text}",
    input_variables=['question','text']
)

url="https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdhe4hn-a/p/itm8505e2f874525?pid=COMHH78YEUAMB68W&lid=LSTCOMHH78YEUAMB68WGNHGES&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=bc84f9de-2720-46f3-9d8b-fe71b6f34a68.COMHH78YEUAMB68W.SEARCH&ppt=None&ppn=None&ssid=8vi1yr1cog0000001781282026155&ov_redirect=true"
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':"what is  product that we are talking about",'text':docs[0].page_content}))

