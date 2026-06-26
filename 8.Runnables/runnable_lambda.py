from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence,RunnableParallel,RunnableLambda
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

def word_counter(text):
    return len(text.split())


runnable_word_counter = RunnableLambda(word_counter)

joke_gen_chain = RunnableSequence(prompt1,model,StrOutputParser())

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
result = final_chain.invoke({'topic':'cricket'})
print(result)