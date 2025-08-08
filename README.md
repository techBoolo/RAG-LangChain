# LangChain RAG Project with Local LLMs

This project is a modern boilerplate for building Retrieval Augmented Generation (RAG) applications using the LangChain framework. It is pre-configured to run with local models via Ollama, ensuring privacy and cost-effectiveness, while also being set up to easily accommodate other providers like OpenAI, Google, and Anthropic.

The core goal is to provide a clean, scalable foundation for experimenting with and deploying custom Q&A systems over private documents.

## Features (Planned & Included)

-   **Modern Python Tooling**: Uses `uv` for high-speed package and virtual environment management.
-   **Local First**: Pre-configured for use with local LLMs like Llama 3 via [Ollama](https://ollama.com/).
-   **RAG Ready**: Includes `faiss-cpu` for efficient, local vector storage and retrieval.
-   **Up-to-Date LangChain**: Uses the latest modular `langchain-core`, `langchain-ollama`, and other `langchain-*` packages.
-   **Extensible**: Easily configurable for different LLM providers through environment variables.

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

4.  **Set up environment variables:**
    This project uses a `.env` file for API keys. While the primary focus is local, you can add keys for other services.
    ```bash
    # Copy the example file
    cp .env.example .env
    
    # Add any necessary API keys (optional for local-only use)
    # nano .env
    ```

### Running the Application

Currently, the `main.py` file is a simple placeholder. To run it:
```bash
python main.py
```

### Project Structure
.
├── .env.example          # Example environment variables for various LLM providers
├── .gitignore            # Standard Python gitignore
├── .python-version       # Specifies the Python version for tools like pyenv
├── main.py               # The main entry point for the application (currently a placeholder)
├── pyproject.toml        # Project definition and dependencies for uv/pip
└── ...                   # Other experimental or feature files