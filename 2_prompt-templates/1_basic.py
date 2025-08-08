from langchain.prompts import ChatPromptTemplate

# template = "Tell me {number} jokes about {topic}."
message = [
  ("system", "You are a comedian who tells jokes about {topic}."),
  ("human", "Tell me {count} jokes")
]
# prompt_template = ChatPromptTemplate.from_template(template)
prompt_template = ChatPromptTemplate.from_messages(message)

prompt = prompt_template.invoke({"topic": "lawyers", "count": 3})
print(prompt)