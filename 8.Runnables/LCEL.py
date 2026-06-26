from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
import os
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)

prompt1 = PromptTemplate(
    template = 'Generate a tweet about the topic {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt1 | model | parser

result =chain.invoke({'topic':'Balen Shah'})

print(result)

chain.get_graph().print_ascii()