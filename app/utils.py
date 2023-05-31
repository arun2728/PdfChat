import os
from PyPDF2 import PdfReader
from tqdm import tqdm
from typing import List
from langchain.docstore.document import Document

def read_pdf(pdf_file: str) -> List[Document]:
    
    if not os.path.isfile(pdf_file):
        raise FileExistsError(f"{pdf_file} is not found!!!")

    # Create a pdf reader object
    print(f"Reading {pdf_file}...")
    reader = PdfReader(pdf_file)
    print(f"No. of pages found: {len(reader.pages)}")

    # Extract text from pages
    return [ 
        Document(
            page_content=page.extract_text(),
            metadata={"source": f"Page {i + 1}"}
        ) 
        for i, page in tqdm(enumerate(reader.pages))
    ]
    
    
