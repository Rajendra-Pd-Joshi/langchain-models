from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

Loader = TextLoader('9.Document-loader/cricket.txt',encoding = 'utf-8')

documents = Loader.load()

prompt = PromptTemplate(
    template = 'write an summary about the poem {poem}',
    input_variables = ['poem']
)

parser = StrOutputParser()

model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)


chain = prompt | model | parser

result = chain.invoke({'poem':documents[0].page_content})

print(result)

