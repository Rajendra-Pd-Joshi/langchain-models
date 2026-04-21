from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

documents=[
    "what is the capital of nepal?",
    "who is the Balen shah",
    "do you know about Hami Nepal Organization and sudan gurung"
]

embeddings=OpenAIEmbeddings(
    model=os.getenv("Embedding_model"),
    dimensions=32
)


response=embeddings.embed_documents(documents)

print(str(response))