import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_directory, "docs", "vscode-mac.pdf")
persistence_directory = os.path.join(current_directory, "db")

if not os.path.exists(pdf_path):
    print(f"Error: The file '{pdf_path}' was not found.")
else:
    # loading document
    print("Loading the PDF document...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Successfully loaded the document.")
    print(f"The PDF has {len(documents)} pages.")

    # splitting
    print("\nSplitting the document into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Successfully split the document into {len(chunks)} chunks.")

    # embedding
    print("\nSetting up the embedding model...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    print("Embedding model set up successfully.")

    print("\nCreating and saving the FAISS vector store...")
    try:
        os.makedirs(persistence_directory, exist_ok=True)
        vector_store = FAISS.from_documents(chunks, embeddings)
        vector_store.save_local(persistence_directory)
        print("FAISS vector store created and saved successfully.")
    except Exception as e:
        print(f"An error occurred while creating the vector store: {e}")