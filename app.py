# app.py
import streamlit as st
from pdf_loader import load_pdf_to_vectorstore
from qa_engine import get_qa_chain

st.title("📚 PDF Question Answering App (Local)")

pdf = st.file_uploader("Upload a PDF", type="pdf")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    vectordb = load_pdf_to_vectorstore("temp.pdf")
    qa = get_qa_chain(vectordb)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = qa.run(question)
        st.write("🧠 Answer:", answer)
