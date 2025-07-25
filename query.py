from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_core.documents import Document

# Load vector DB
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vector_db", embedding_model, allow_dangerous_deserialization=True)

# Load local model for answering (open-source, no key)
model_name = "google/flan-t5-small"  # You can also try flan-t5-base or mistralai/Mistral-7B-Instruct-v0.1 if your machine supports it
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
qa_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Prompt user
query = input("You: ")

# Find relevant documents
docs = vectorstore.similarity_search(query, k=3)
context = "\n\n".join([doc.page_content for doc in docs])

# Build prompt for LLM
prompt = f"Answer the question based on the logs below:\n\n{context}\n\nQuestion: {query}\nAnswer:"

# Generate answer
response = qa_pipeline(prompt, max_new_tokens=256, do_sample=False)[0]["generated_text"]

# Output
print(f"Assistant: {response}")
