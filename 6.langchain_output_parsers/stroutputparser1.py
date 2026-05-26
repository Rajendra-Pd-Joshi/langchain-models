import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

# Prompt template
template1= PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=['topic']
)

# output parser
output_parser= StrOutputParser()

# Prompt Template
template2= PromptTemplate(
    template="Write a five-line summary of the following text:\n\n{text}",
    input_variables=['text']
)

# chain
chain= template1 | model |output_parser | template2 | model | output_parser

result=chain.invoke({
    'topic': "Nepal and Himalayas"
})
print("\n===== SUMMARY =====\n")
print(result)
