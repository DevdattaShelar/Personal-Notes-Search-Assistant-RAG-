## 🗂 Folder Structure

project/
│── app.py
│── rag_pipeline.py
│── build_vector_db.py
│── requirements.txt
│── data/ # Place your PDFs/TXT files here
│── faiss_db/ # Auto-generated vector DB

# 📚 Offline Personal Notes Search Assistant (RAG + Ollama + Streamlit)

An offline **Retrieval-Augmented Generation (RAG)** application that allows you to
search your **own PDF / TXT notes** using fully **local** AI models.

No API keys.  
No internet needed.  
Everything runs *offline* using **Ollama**, **FAISS**, and **Streamlit**.

---

## 🚀 Features

### ✔ 100% Offline  
Uses **local LLMs** and **local embeddings** — nothing is sent online.

### ✔ Works with Your Documents  
Supports:
- PDF files  
- TXT files  

Just place them inside the `data/` folder.

### ✔ Local Vector Database (FAISS)  
Your notes are embedded using:
- `all-minilm:33m` (local embedding model)

### ✔ Local LLM for answering  
By default uses:
- `qwen2:1.5b` (via Ollama)

### ✔ Clean & Simple UI  
Built with Streamlit.

---

## 🛠 Prerequisites

### 1️⃣ Install Python 3.10+  
https://www.python.org/downloads/

### 2️⃣ Install Ollama  
Download here:  
https://ollama.com/download

---

## 🤖 Install Required Models in Ollama

Run these commands:

```sh
ollama pull all-minilm:33m
ollama pull qwen2:1.5b
