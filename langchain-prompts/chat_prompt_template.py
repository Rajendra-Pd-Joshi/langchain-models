from langchain_core.prompts import ChatPromptTemplate
chat_template=ChatPromptTemplate.from_messages([
    ("system","you are a expert in {field}"),
    ("human","explain the concept of {topic} in simple terms")
])

prompt=chat_template.invoke({
    'field': 'cricket',
    'topic': 'dusra'
})

print(prompt)