import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from langchain_core.runnables import RunnableParallel ,RunnableBranch, RunnableLambda


load_dotenv()

# Initialize model
model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)


class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='what is the sentiment of the following feedback\n {text}')

parser1 = StrOutputParser()
parser2= PydanticOutputParser(pydantic_object = Feedback)


prompt1 = PromptTemplate(
    template = 'Give me the sentiment of the following feedback \n {text} {format_instruction}',
    input_variables = ['text'],
    partial_variables= {'format_instruction' : parser2.get_format_instructions()}
)


sentiment_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'write the reply for this positive review \n {review}',
    input_variables = ['review']
)
prompt3 = PromptTemplate(
    template = 'write the reply for this negative review \n {review}',
    input_variables = ['review']
)

reply_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , prompt2 | model | parser1),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: 'sentiment is not classified yet')
)

chain = sentiment_chain | reply_chain

result = chain.invoke({'text':'this is the confortable blanket for single bed'})

print(result)

chain.get_graph().print_ascii()