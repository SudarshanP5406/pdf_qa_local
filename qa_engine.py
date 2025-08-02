# qa_engine.py
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def get_qa_chain(vectordb):
    llm = Ollama(model="nomic-embed-text")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa_chain
