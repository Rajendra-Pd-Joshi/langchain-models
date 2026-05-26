from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize model
model = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.3
)

# Prompt 1: Detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)

# Prompt 2: Summary
template2 = PromptTemplate(
    template="Write a five-line summary of the following text:\n\n{text}",
    input_variables=["text"]
)

# Generate first prompt
prompt1 = template1.invoke({
    "topic": "Black Hole"
})

# Get detailed report
result1 = model.invoke(prompt1)

print("\n===== DETAILED REPORT =====\n")
print(result1.content)

# Generate second prompt using first result
prompt2 = template2.invoke({
    "text": result1.content
})

# Get summary
result2 = model.invoke(prompt2)

print("\n===== SUMMARY =====\n")
print(result2.content)