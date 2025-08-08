# LangChain Project Examples with Local LLMs

This project is a collection of examples for building applications with the LangChain framework. It is pre-configured to run with local models via Ollama, ensuring privacy and cost-effectiveness.

The core goal is to provide a clean, scalable foundation for experimenting with and deploying custom Q&A systems and conversational agents. The examples progress from simple, single-shot generation to fully persistent, multi-turn conversations.

## Features

-   **Modern Python Tooling**: Uses `uv` for high-speed package and virtual environment management.
-   **Local First**: Pre-configured for use with local LLMs like Llama 3 via [Ollama](https://ollama.com/).
-   **RAG Ready**: Includes `faiss-cpu` for efficient, local vector storage and retrieval (planned for future examples).
-   **Up-to-Date LangChain**: Uses the latest modular `langchain-core`, `langchain-ollama`, and other `langchain-*` packages.
-   **Practical Examples**: Includes runnable scripts demonstrating single-turn generation, in-memory conversations, and conversations with persistent database history.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.12+
-   [uv](https://github.com/astral-sh/uv) (for package management)
-   [Ollama](https://ollama.com/) installed and running.
-   A local model pulled via Ollama (e.g., `ollama pull llama3`).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Create and activate a virtual environment using `uv`:**
    ```bash
    # Create the virtual environment
    uv venv

    # Activate it (on macOS/Linux)
    source .venv/bin/activate
    
    # Or on Windows (PowerShell)
    # .venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies:**
    `uv` will read the `pyproject.toml` file and install all necessary packages.
    ```bash
    uv pip install .
    ```

4.  **Set up environment variables (Optional):**
    This project primarily uses local models. However, if you plan to use hosted services, you can add your keys to a `.env` file.
    ```bash
    # Copy the example file
    cp .env.example .env
    
    # Add any necessary API keys to .env
    # nano .env
    ```

---

## Usage / Running the Examples

This project contains several standalone scripts, each demonstrating a different LangChain concept.

### 1. Simple Generation (`2_simple-generate.py`)
Demonstrates the most basic interaction: sending a single prompt to the LLM and printing the response.

**To run:**
```bash
python 2_simple-generate.py
```

### 2. Basic Conversation (`3_basic-conversation.py`)
Shows how a conversational history can be manually constructed and sent to the LLM to provide context for a follow-up question. It is not interactive.

**To run:**
```bash
python 3_basic-conversation.py
```

### 3. Interactive In-Memory Chat (`4_realtime-conversation.py`)
Launches an interactive chat session in your terminal. It manages a chat history list **in memory**, allowing the LLM to remember previous parts of the conversation for the duration of the session. The history is lost when the script ends.

**To run:**
```bash
python 4_realtime-conversation.py
```

### 4. Interactive Persistent Chat (`5_persistent-conversation.py`)
This is the most advanced example. It launches an interactive chat that **saves the entire conversation to a local SQLite database (`chat_history.db`)**. When you restart the script, the history is loaded, allowing you to resume conversations across sessions.

**To run:**
```bash
python 5_persistent-conversation.py
```

---

## Project Structure

```
.
├── .env.example                # Example environment variables for various LLM providers
├── .gitignore                  # Standard Python gitignore
├── .python-version             # Specifies the Python version (3.12)
├── 2_simple-generate.py        # Example: Basic, one-shot LLM invocation
├── 3_basic-conversation.py     # Example: Manually constructing conversation history
├── 4_realtime-conversation.py  # Example: An interactive chat with in-memory history
├── 5_persistent-conversation.py # Example: An interactive chat with persistent SQLite history
├── main.py                     # A placeholder entry point for a future, larger application
├── pyproject.toml              # Project definition and dependencies
└── README.md                   # This file
```