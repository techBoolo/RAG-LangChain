from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

# template = "Tell me {number} jokes about {topic}."
message = [
  ("system", "You are a comedian who tells jokes about {topic}."),
  HumanMessage(content="Tell me 3 joks")
  # ("user", "Tell me {count} jokes")
]
# prompt_template = ChatPromptTemplate.from_template(template)
prompt_template = ChatPromptTemplate.from_messages(message)

prompt = prompt_template.invoke({"topic": "lawyers", "count": 3})
print(prompt)