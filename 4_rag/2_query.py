import os
import sys
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PERSISTENCE_PATH = os.path.join(BASE_DIR, "db")
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3"

# 1. Load the existing vector store
print("Attempting to load vector store...")
if not os.path.exists(PERSISTENCE_PATH):
    print(f"Error: Vector store not found at '{PERSISTENCE_PATH}'.")
    print("Please run the ingestion script (1_ingest.py) first.")
    sys.exit(1)

try:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_store = FAISS.load_local(
        PERSISTENCE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("Vector store loaded successfully.")
    print(f"Number of vectors in store: {vector_store.index.ntotal}")
except Exception as e:
    print(f"An error occurred while loading the vector store: {e}")
    sys.exit(1)

# 2. Create a retriever for the vector store
retriever = vector_store.as_retriever()
print("Retriever created successfully.")

# 3. RAG prompt template
template = """
You are an expert assistant for answering questions.
You must answer the question based only on the provided context.
If you don't know the answer from the context, just say that you don't know. Do not make up an answer.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

prompt = ChatPromptTemplate.from_template(template)
print("RAG prompt template created.")

# 4. build the RAG chain
llm = ChatOllama(model=LLM_MODEL)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
print("RAG chain built successfully.")