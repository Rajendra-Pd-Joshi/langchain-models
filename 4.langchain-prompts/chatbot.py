from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import os

load_dotenv()

model= ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=1.5,
)

chat_history=[
    SystemMessage(content='you are a philoshoper')
]

while True:
    user_input=input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break;
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))  
    print("AI: ",result.content)

print(chat_history)