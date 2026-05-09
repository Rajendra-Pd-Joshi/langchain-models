from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model= ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=1.5,
)

messages=[
    SystemMessage(content='you are a philoshoper'),
    HumanMessage(content='tell me about osho')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)