from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from .utils import read_pdf
from typing import List
from langchain.docstore.document import Document

embeddings = OpenAIEmbeddings()

def main():
    
    pdf_file: str = input("Pdf file path: ")
    
    # Get documents
    documents: List[Document] = read_pdf(pdf_file=pdf_file)

    # Create index file
    docsearch = Chroma.from_documents(documents, embeddings)
    
    # Create retriever
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())
    
    while True:
        query: str = input("Enter your query: ")
        response: str = qa.run(query).strip(" ")
        print(f"Response: {response}")
    
    
if __name__ == "__main__":
    main()
