import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)

prompt = PromptTemplate(
    template = 'write a joke about the topic {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

result = chain.invoke({'topic':'India'})

print(result)
