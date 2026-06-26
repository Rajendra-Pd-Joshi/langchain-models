from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough
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
    template = 'Generate a detail report about the topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a summary about the text {text}',
    input_variables=['text']
)

parser = StrOutputParser()

report_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) >300 ,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)


final_chain = RunnableSequence(report_chain,branch_chain)

print(final_chain.invoke({'topic':'Nepal'}))

final_chain.get_graph().print_ascii()