import sqlite3
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Database Setup ---
DB_FILE = "chat_history.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# --- Language Model Setup ---
llm = ChatOllama(model="llama3")

# --- Chat History Management ---
def load_chat_history():
    """Loads chat history from the database."""
    cursor.execute("SELECT role, content FROM chat_history ORDER BY timestamp ASC")
    rows = cursor.fetchall()
    history = []
    for row in rows:
        role, content = row
        if role == 'system':
            history.append(SystemMessage(content=content))
        elif role == 'human':
            history.append(HumanMessage(content=content))
        elif role == 'ai':
            history.append(AIMessage(content=content))
    return history

def save_message(role, content):
    """Saves a message to the database."""
    cursor.execute("INSERT INTO chat_history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()

# --- Main Chat Logic ---
goodbye_message = ['quit', 'bye', 'good bye', 'end', 'stop', 'leave', 'exit']
initial_prompt = f"""
You are a helpful assistant,
and you have to say good bye only when the user uses the exact phrase.
The phrases that trigger goodbye are: {', '.join(goodbye_message)}
"""

chat_history = load_chat_history()

# If history is empty, add the initial system prompt
if not any(isinstance(msg, SystemMessage) for msg in chat_history):
    system_message = SystemMessage(content=initial_prompt)
    chat_history.insert(0, system_message)
    save_message('system', initial_prompt)


print("Chat with your AI assistant. Type one of the following to exit:", ', '.join(goodbye_message))

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in goodbye_message:
            print("Assistant: Goodbye!")
            break

        # Add user message to history and save it
        chat_history.append(HumanMessage(content=user_input))
        save_message('human', user_input)

        # Get AI response
        response = llm.invoke(chat_history)
        ai_response_content = response.content

        # Add AI response to history and save it
        chat_history.append(AIMessage(content=ai_response_content))
        save_message('ai', ai_response_content)

        print(f"Assistant: {ai_response_content}")

    except KeyboardInterrupt:
        print("\nAssistant: Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Close the database connection when the loop ends
conn.close()
