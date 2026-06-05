import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
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

# parser
parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me 5 facts about {topic} \n {format_instructions}',
    input_variables = ['topic'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}

)
# method 1 with out using the chain concepts
# prompt = template.format(topic = "Nepal and Himalayas")

# # print(prompt)

# result = model.invoke(prompt)

# # print(result)

# parsed_result = parser.parse(result.content)

# print(type(parsed_result))


# method 2 using the chain concepts

chain = template | model | parser

result = chain.invoke({
    'topic': 'Nepal and Himalayas'
})

print(result)