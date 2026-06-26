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
prompt2 = PromptTemplate(
    template = 'Generate a linkdin post  about the topic {topic}',
    input_variables=['topic']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkdin_post':RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'Balen Shah'})

print(result)

parallel_chain.get_graph().print_ascii()