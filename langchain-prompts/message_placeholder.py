from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat template
chat_template=ChatPromptTemplate([
    ('system','you are a helpfull ai assistant'),
    MessagesPlaceholder(variable_name='history'),
    ('human','{query}')
])

# load history
history=[]

with open('chat_history.txt') as f:
    history.extend(f.readlines())

print(history)

# create prompt

prompt=chat_template.invoke({
    'history':history,
    'query':'what is the status of my refund?'
})

print(prompt)