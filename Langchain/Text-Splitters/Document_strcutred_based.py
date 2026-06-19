from langchain_text_splitters import RecursiveCharacterTextSplitter , Language

text = """
# Introduction to Artificial Intelligence

Artificial Intelligence (AI) is a field of computer science focused on creating systems that can perform tasks requiring human intelligence.

## Key Areas of AI

### Machine Learning
Machine Learning enables computers to learn from data without being explicitly programmed.

### Deep Learning
Deep Learning uses neural networks with multiple layers to identify complex patterns in data.

### Natural Language Processing
NLP helps computers understand and generate human language.

## Applications

- Chatbots
- Recommendation Systems
- Self-driving Cars
- Medical Diagnosis

## Example Python Code

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Shubham"))"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size = 200,
    chunk_overlap=0,
)

chunk = splitter.split_text(text)
print(len(chunk))
print(chunk[0])