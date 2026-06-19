import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Initialize model
model = ChatOpenAI(
    model='openai/gpt-4o-mini',
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0.3
)

prompt1 = PromptTemplate(
    template='Generate a short note on the given topic\n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 question on the given topic and for each question give 4 option basically mcqs\n{text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='give a merged report by merging the short notes {notes} and quiz questions {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 |model |parser
})

merge_chain = prompt3 | model |parser

chain = parallel_chain | merge_chain

result=chain.invoke({'text':'Nepal and gen-z protest'})


print(result)

chain.get_graph().print_ascii()

