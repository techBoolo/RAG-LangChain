from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

# LangChain automatically communicates with your running Ollama instance.
llm = ChatOllama(model="llama3")

# message = [
#   SystemMessage(content="You are a helpful assistant."),
#   HumanMessage(content="what is 9 times 9"), 
# ]

# result = llm.invoke(message)
# print(result.content)

message = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="what is 9 times 9"),
  AIMessage(content="9 times 9 is 81"),
  HumanMessage(content="what is 50 divided by 5?"), 
]

result = llm.invoke(message)
print(result.content)