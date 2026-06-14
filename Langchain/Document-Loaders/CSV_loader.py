from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='customers-100.csv')

docs = loader.load()

print(len(docs))
print(docs[1])


# for every row you get one doc object