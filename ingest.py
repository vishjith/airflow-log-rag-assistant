from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load log file
loader = TextLoader("data/airflow_logs.txt")
documents = loader.load()

# Split by line blocks (good for logs)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=256,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)

docs = text_splitter.split_documents(documents)

# Embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Vector DB
db = FAISS.from_documents(docs, embeddings)
db.save_local("vector_db")

print("Ingestion complete with improved log chunking!")
