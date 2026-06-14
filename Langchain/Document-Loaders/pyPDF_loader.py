from langchain_community.document_loaders import  PyPDFLoader 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

loader = PyPDFLoader('Script.pdf')
docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

#if u wished to use pdfs with tablee/columns use PDFPlumberLoader
#if u wished to use pdfs with scanned images use UnstructuredPDFLoader or AmazonTextracterPDFLoader
#if u wished to use pdfs with need layout and image data use PyMuPDFLoader
#if u wished to use pdfs and want beest structure extraction use UnstructuredPDFLoader
