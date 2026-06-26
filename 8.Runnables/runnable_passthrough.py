from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
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
    template = 'give a joke about the topic {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = 'explain the following joke  {response}',
    input_variables=['response']
)


parser = StrOutputParser()



joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
result = final_chain.invoke({'topic':'cricket'})
print(result)

final_chain.get_graph().print_ascii()