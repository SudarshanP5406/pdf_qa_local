import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
import tempfile
import os

# Function to load and split PDF
def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)

# Build retriever and QA chain
def get_qa_chain(docs):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    llm = Ollama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

# Streamlit UI
st.set_page_config(page_title="Local PDF Q&A App", layout="centered")
st.title("📄 Local PDF Q&A with Mistral")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about the PDF")

if uploaded_file and question:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    with st.spinner("Processing PDF and finding answer..."):
        docs = process_pdf(tmp_file_path)
        qa = get_qa_chain(docs)
        answer = qa.run(question)

    os.remove(tmp_file_path)
    st.success("Answer:")
    st.write(answer)
