from pinecone import ServerlessSpec
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf_files,text_split,download_embedding,filter_docx
import os
load_dotenv()


extracted_data=load_pdf_files(data="data/")
filter_data=filter_docx(extracted_data)
texts_chunks =text_split(filter_data)




pc = Pinecone(api_key=os.environ.get("PINE_CONE_KEY"))
# Map PINE_CONE_KEY to what LangChain expects
os.environ["PINECONE_API_KEY"] = os.environ.get("PINE_CONE_KEY")

index_name="medbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
    )
index=pc.Index(index_name)

# Download the embedding model
embedding = download_embedding()

doc_search = PineconeVectorStore.from_documents(
    embedding=embedding,
    index_name=index_name,
    documents=texts_chunks
)