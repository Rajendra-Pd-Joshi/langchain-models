import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel ,Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Initialize model
model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)

class Person(BaseModel):
    name: str =Field(description='Name of the person')
    age: int =Field(gt=18,description='age of the person')
    city: str =Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name ,age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'Nepal'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content) 

# print(final_result)

chain = template | model | parser

final_result = chain.invoke({'place':'Nepal'})

print(final_result)


# # summary
# str -> stirng
# json -> json -> no schema validation
# structured -> json -> schema validation but no data validation
# pydantic -> json -> schema validation + data validation