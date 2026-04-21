from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings=OpenAIEmbeddings(
    model=os.getenv("Embedding_model"),
    dimensions=32
)

response=embeddings.embed_query("what is the capital of nepal?")

print(str(response))