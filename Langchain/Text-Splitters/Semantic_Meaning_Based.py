from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv


load_dotenv()
embedding = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")
text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)



text = """
Artificial Intelligence is a branch of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence. Examples include image recognition, speech processing, and decision making.

Machine Learning is a subset of Artificial Intelligence. It allows computers to learn patterns from data and improve their performance without being explicitly programmed. Common algorithms include decision trees, random forests, and support vector machines.

Deep Learning is a specialized area of Machine Learning that uses neural networks with many layers. It is widely used in image classification, natural language processing, and speech recognition.

The Solar System consists of the Sun and all objects that orbit it. These include eight planets, dwarf planets, asteroids, comets, and moons.

Earth is the third planet from the Sun and the only known planet to support life. About 71% of Earth's surface is covered by water.

Mars is often called the Red Planet because of its reddish appearance. Scientists are interested in Mars because it may have once supported microbial life.

Cricket is one of the most popular sports in the world. It is played between two teams of eleven players each and is especially popular in India, Australia, and England.

In cricket, a batsman tries to score runs while the bowler attempts to dismiss the batsman. Formats of the game include Test matches, One Day Internationals, and T20 matches.

The Indian Premier League (IPL) is one of the most successful T20 cricket leagues in the world. It features players from different countries competing in franchise-based teams.
"""

docs = text_splitter.create_documents([text])
print(len(docs))
print(docs)