from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
# Load environment variables
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
# LangChain automatically communicates with your running Ollama instance.
llm = ChatOllama(model="llama3")

message = [
    ("system", "You are a comedian who tells jokes about {topic}."),  
    HumanMessage(content="Tell me 3 joks")
]
prompt_template = ChatPromptTemplate.from_messages(message)

prompt = prompt_template.invoke({"topic": "lawyers"})
print(prompt)

result = llm.invoke(prompt)
print(result.content)