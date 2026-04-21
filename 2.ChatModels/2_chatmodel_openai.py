from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    temperature=1.5,
   
    )

response=model.invoke('write a five line poem in cricket?')

print(response.content)