from setuptools import find_packages, setup

setup(
    name="R.A.G",
    version="0.1.0",
    author="Your Name",
    author_email="Gulmohargautam2005@gmail.com", 
    description="A Retrieval-Augmented Generation (R.A.G) system for medical applications.",
    packages=find_packages(),
    install_requires=[
        "langchain==0.3.26",
        "flask==3.1.1",
        "sentence-transformers==2.2.2",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0",
        "lanchain-pinecone==0.2.8",
        "lanchain-openai==0.2.8",
        "langchain-groq",
        "lanchain-community==0.3.26"
    ],
)