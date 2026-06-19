import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
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


schema = [
    ResponseSchema(name = 'fact_1', description ='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description ='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template ='Give 3 facts about {topic}\n {format_instruction}',
    input_variables=['topic'],
    partial_variables ={'format_instruction':parser.get_format_instructions()}
)

# prompt =template.invoke({'topic':'black hole'})

# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)

chain = template | model | parser

result = chain.invoke({'topic':'Nepal and gen-z protest'})

print(result)