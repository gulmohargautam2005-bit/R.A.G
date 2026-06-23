from flask import Flask, render_template, jsonify, request
from src.helper import  download_embedding
from src.prompt import  system_prompt
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import sys

load_dotenv()

# Safely set environment variables — guard against None to prevent TypeError
groq_key = os.getenv("GROQ_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY") or os.getenv("PINE_CONE_KEY")

if not groq_key:
    print("ERROR: GROQ_API_KEY is not set. Exiting.", flush=True)
    sys.exit(1)

if not pinecone_key:
    print("ERROR: PINECONE_API_KEY is not set. Exiting.", flush=True)
    sys.exit(1)

os.environ["GROQ_API_KEY"] = groq_key
os.environ["PINECONE_API_KEY"] = pinecone_key

print("✓ Environment variables loaded successfully", flush=True)

# load existing index
try:
    print("Loading embedding model...", flush=True)
    embedding = download_embedding()
    print("✓ Embedding model loaded", flush=True)

    index_name = "medbot"
    print(f"Connecting to Pinecone index '{index_name}'...", flush=True)
    doc_search = PineconeVectorStore(
        embedding=embedding,
        index_name=index_name
    )
    retriever = doc_search.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    print("✓ Pinecone connected", flush=True)

    chatmodel = ChatGroq(model="llama-3.3-70b-versatile")
    print("✓ ChatGroq initialized", flush=True)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    question_answered_chain = create_stuff_documents_chain(chatmodel, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answered_chain)
    print("✓ RAG chain ready", flush=True)

except Exception as e:
    print(f"FATAL ERROR during startup: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg, flush=True)

    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"], flush=True)

    return str(response["answer"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)