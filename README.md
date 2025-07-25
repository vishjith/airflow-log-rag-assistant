#  Airflow Log RAG Assistant

A local, privacy-first Retrieval-Augmented Generation (RAG) chatbot that allows you to ask natural language questions over your Apache Airflow logs. No OpenAI key or external API is required — powered entirely by local HuggingFace embeddings and FAISS.

---

##  Features

- 📄 Parses and indexes Apache Airflow logs
- 🤖 Answers questions about errors, DAG runs, and logs using natural language
- 🧠 Uses local HuggingFace embeddings (`all-MiniLM-L6-v2`) via `langchain_huggingface`
- 🔎 Fast similarity search powered by FAISS
- 🔐 No external API usage — no OpenAI key needed

---

##  Project Structure
```bash
airflow-log-rag-assistant/
├── data/
│ └── airflow_logs.txt # Raw Airflow logs (input)
├── ingest.py # Script to load logs, embed and index with FAISS
├── query.py # Script to query the logs in natural language
├── .env.example # Placeholder for environment config (no secrets)
├── requirements.txt # Python dependencies
```

### 1. Clone the Repository

```bash
git clone https://github.com/vishjith/airflow-log-rag-assistant.git
cd airflow-log-rag-assistant
```
### 2. Set Up the Environment

```python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
### 3. Add Your Airflow Logs
Place your logs in the data/airflow_logs.txt file. For example:

```[2025-07-15 10:31:42,123] {taskinstance.py:123} ERROR - Task failed due to ...```

### 4. Run the Ingestion Script
This script splits, embeds, and indexes the logs:

```python ingest.py```

### 5. Ask Questions About Logs
```
python query.py
```
### Dependencies
- langchain
- langchain_community
- langchain_huggingface
- transformers
- faiss-cpu

### Install via:

```pip install -r requirements.txt```

### Credits
[LangChain](https://github.com/langchain-ai/langchain)  
[HuggingFace Transformers](https://huggingface.co/)  
[FAISS](https://github.com/facebookresearch/faiss)



