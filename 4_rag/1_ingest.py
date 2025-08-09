import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

current_directory = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_directory, "docs", "vscode-mac.pdf")

if not os.path.exists(pdf_path):
    print(f"Error: The file '{pdf_path}' was not found.")
else:
    print("Loading the PDF document...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Successfully loaded the document.")
    print(f"The PDF has {len(documents)} pages.")

    print("\nSplitting the document into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Successfully split the document into {len(chunks)} chunks.")

    if chunks:
        print("\n--- Content of the first chunk: ---")
        print(chunks[0].page_content)
        
        print("\n--- Metadata of the first chunk: ---")
        # Notice that the metadata is preserved from the original document
        print(chunks[0].metadata)