from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

from pdf_loader import load_pdf

def generate_answer(pdf_path, question):
    # Load and split PDF
    docs = load_pdf(pdf_path)

    # Create embeddings using Ollama
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = FAISS.from_documents(docs, embeddings)

    # Load Mistral from Ollama
    llm = Ollama(model="mistral")

    # Create a Retrieval-based QA chain
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Ask the question
    result = qa.run(question)
    return result
