# pdf_loader.py
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def load_pdf_to_vectorstore(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(docs, embeddings)

    return vectordb
