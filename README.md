📚 Local PDF Question Answering App
A fully local Question-Answering (QA) app where you can upload a PDF and ask questions about its content. Built with LLaMA 2 via Ollama and LangChain, the app processes everything offline — keeping your data private and secure.

💡 Perfect for reading research papers, manuals, textbooks, or long reports!

🧠 Key Features
Upload and analyze any PDF document

Ask natural language questions about its content

Powered by LLaMA 2 running locally (no internet required)

Uses embeddings + vector search for accurate results

Clean UI built with Streamlit

🛠️ Tech Stack
LLM: LLaMA 2 (via Ollama)

PDF Parsing: PyPDFLoader (via LangChain)

Embeddings & Search: Ollama Embeddings + Chroma Vector Store

Frontend: Streamlit

Language: Python 3.x

📦 Installation Instructions
1. Install Ollama and Download LLaMA 2
Download Ollama from https://ollama.com/download, then run:
ollama pull llama2

2. Clone this Repository
git clone https://github.com/your-username/pdf-qa-local.git
cd pdf-qa-local

3. Install Python Dependencies
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

A browser window will open where you can upload a PDF and ask questions.
