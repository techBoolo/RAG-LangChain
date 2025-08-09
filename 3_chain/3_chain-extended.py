from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3")

# template = "Tell me {number} jokes about {topic}."
message = [
  ("system", "You are a comedian who tells jokes about {topic}."),
  HumanMessage(content="Tell me 3 joks")
  # ("user", "Tell me {count} jokes")
]
prompt_template = ChatPromptTemplate.from_messages(message)

uppercase = RunnableLambda(lambda x: x.upper())
count = RunnableLambda(lambda x: f"{len(x.split())}\n{x}")

chain = prompt_template | llm | StrOutputParser() | uppercase | count
result = chain.invoke({"topic": "lawyers", "count": 3})
print(result)


