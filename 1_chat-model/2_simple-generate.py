from langchain_ollama import ChatOllama
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# LangChain automatically communicates with your running Ollama instance.
llm = ChatOllama(model="llama3")

result = llm.invoke("who are you? What is 81 divided by 9?, and what is the capital of France? can i ask you any question?")
print(result.content)
print(result)