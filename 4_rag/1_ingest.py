import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "docs", "vscode-mac.pdf")
PERSISTENCE_PATH = os.path.join(BASE_DIR, "db")
EMBEDDING_MODEL = "nomic-embed-text"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

if os.path.exists(os.path.join(PERSISTENCE_PATH, "index.faiss")):
    print(f"Vector store already exists at '{PERSISTENCE_PATH}'. No action taken.")
    sys.exit(0)
print("Vector store not found. Starting ingestion process...")

if not os.path.exists(PDF_PATH):
    print(f"Error: The file '{PDF_PATH}' was not found.")
    sys.exit(1)
else:
    # loading document
    print("Loading the PDF document...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    print(f"Successfully loaded the document. The PDF has {len(documents)} pages.")

    # splitting
    print("\nSplitting the document into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Successfully split the document into {len(chunks)} chunks.")

    # embedding
    print("\nSetting up the embedding model...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    print(f"Embedding model '{EMBEDDING_MODEL}' set up successfully.")

    # save to vector store
    print(f"\nCreating and saving the FAISS vector store at '{PERSISTENCE_PATH}'...")
    try:
        os.makedirs(PERSISTENCE_PATH, exist_ok=True)
        vector_store = FAISS.from_documents(chunks, embeddings)
        vector_store.save_local(PERSISTENCE_PATH)
        print("FAISS vector store created and saved successfully.")
    except Exception as e:
        print(f"An error occurred while creating the vector store: {e}")
        sys.exit(1)