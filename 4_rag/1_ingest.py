import os
from langchain_community.document_loaders import PyPDFLoader

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

    if documents:
      print("\n--- Content of the first page: ---")
      print(documents[0].page_content[:500]) # Print the first 500 characters
        
      print("\n--- Metadata of the first page: ---")
      print(documents[0].metadata)