from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatOllama(model="llama3")

chat_history = []
goodbye_message = ['quit', 'bye', 'good bye', 'end', 'stop', 'leave', 'exit']
initial_prompt =f"""
You are a helpful assistant, 
and you have to say good bye only when the user uses the exact phrase. 
The phrases that trigger goodbye are: {', '.join(goodbye_message)}
"""
system_message = SystemMessage(content=initial_prompt)
chat_history.append(system_message)

while True:
    user_input = input("User: ")
    if(user_input.lower() in goodbye_message):
        break
    chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    
    print(f"Assistant: {response.content}")


