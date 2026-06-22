
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"
from langchain_community.document_loaders import TextLoader,PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import  List
from langchain.schema import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
import torch
# loading the documents
def load_pdf_files(data):
    loader =DirectoryLoader(
        data,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents


# filter the documnets
def filter_docx(docs: List[Document])-> List[Document]:
    """
    given a list of documnets objects,eturn a new list of document objects
    containing oly source ain metadata and the original page_content.
    """
    minimal_docs: List[Document]=[]
    for doc in docs :
        src=doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return minimal_docs

# split document into smaller chunks
def text_split(minimal_docx):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    texts_chunks=text_splitter.split_documents(minimal_docx)
    return texts_chunks
#  downloading the model

def download_embedding():
    """download and return hugging face embedding model"""
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    embeddings=HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device":"cuda" if torch.cuda.is_available() else "cpu"}
    )
    return embeddings



