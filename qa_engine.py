# qa_engine.py
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def get_qa_chain(vectordb):
    llm = Ollama(model="llama2")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa_chain
