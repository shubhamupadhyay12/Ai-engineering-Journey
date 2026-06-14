from langchain_community.document_loaders import DirectoryLoader  , PyPDFLoader


loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
    


#load fucntion is used for less no. of pdf
#lazy_load used when working with more pdfs 