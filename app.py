from flask import Flask, render_template, jsonify, request
from src.helper import  download_embedding
from src.prompt import  system_prompt
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from src.prompt import *
import os
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY") or os.getenv("PINE_CONE_KEY")

# load existing index
embedding=download_embedding()
index_name="medbot"

doc_search=PineconeVectorStore(
    embedding=embedding,
    index_name=index_name
)
retriever=doc_search.as_retriever(search_type="similarity",search_kwargs={"k":3})
chatmodel=ChatGroq(model ="llama-3.3-70b-versatile")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answered_chain=create_stuff_documents_chain(chatmodel,prompt)
rag_chain=create_retrieval_chain(retriever,question_answered_chain)

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])

    return str(response["answer"])


if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)