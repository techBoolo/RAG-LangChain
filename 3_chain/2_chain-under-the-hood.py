from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda, RunnableSequence

llm = ChatOllama(model="llama3")

# template = "Tell me {number} jokes about {topic}."
message = [
  ("system", "You are a comedian who tells jokes about {topic}."),
  HumanMessage(content="Tell me 3 joks")
  # ("user", "Tell me {count} jokes")
]
prompt_template = ChatPromptTemplate.from_messages(message)


format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: llm.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# three steps to create a chain(first, middle, last)
# chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)
chain = RunnableSequence(format_prompt, invoke_model, parse_output)

result = chain.invoke({"topic": "lawyers", "count": 3})
print(result)
