import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_directory, "docs", "vscode-mac.pdf")

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
