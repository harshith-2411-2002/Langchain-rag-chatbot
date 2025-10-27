# 🧠 LangChain RAG Chatbot (Local AI Assistant using Ollama + FAISS)

### 🚀 Intelligent, Offline, Document-Aware Chatbot built with LangChain, Ollama (Mistral), FAISS, and HuggingFace Embeddings

---

## 📘 Overview

This project is a **Retrieval-Augmented Generation (RAG)** chatbot that can **read, understand, and answer questions from any set of PDF documents** — entirely **offline**.

It uses **LangChain for orchestration**, **FAISS** for vector search, and **Ollama (Mistral LLM)** as a local reasoning engine.
You can upload new data anytime using a **parallel Flask app**, allowing the system to continuously learn and respond intelligently from the latest context.

---

## 🎯 Key Features

✅ **Offline Intelligence** — No API calls or internet required; all LLM processing happens locally using Ollama.
✅ **RAG Pipeline** — Combines document retrieval (FAISS) with context-aware generation (Mistral).
✅ **Real-time Knowledge Updates** — Add new information dynamically through a separate web interface.
✅ **GPU Acceleration** — Uses CUDA-enabled HuggingFace embeddings for lightning-fast vector operations.
✅ **Multi-Interface Architecture** —

* `app.py` → Chatbot interface for querying documents
* `app2.py` → Input app to add new knowledge
  ✅ **Scalable Design** — Modular code that supports new models or embedding upgrades easily.
  ✅ **Privacy-Focused** — All computation and data remain on your local system.

---

## 🏗️ Tech Stack

| Category     | Technology                                             |
| ------------ | ------------------------------------------------------ |
| Language     | Python 3.10+                                           |
| Frameworks   | Flask, LangChain                                       |
| Embeddings   | HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS                                                  |
| LLM          | Ollama (Mistral 7B)                                    |
| GPU Support  | CUDA 12.8                                              |
| Data Format  | PDF Documents                                          |
| UI           | HTML + CSS + JS (Lightweight Frontend)                 |

---

## ⚙️ Architecture Overview

```
+------------------------+
|      User Query        |
+-----------+------------+
            |
            v
+------------------------+
|   Flask Chat UI (app)  |
+-----------+------------+
            |
            v
+------------------------+
| LangChain RAG Pipeline |
|  - Retrieve (FAISS)    |
|  - Augment Context     |
|  - Generate (Ollama)   |
+-----------+------------+
            |
            v
+------------------------+
|    Helpful Answer      |
+------------------------+
```

🧩 Parallel app (`app2.py`) lets users insert new data via embeddings and updates FAISS vectors in real time.

---

## 📂 Project Structure

```
githubBNMChatbot/
│
├── app.py                     # Main Flask chatbot app
├── app2.py                    # Data ingestion web app
├── ingest.py                  # Converts PDF data to FAISS vectors
├── model.py                   # LangChain RAG model pipeline
├── user.py                    # Adds new user input to FAISS DB
│
├── data/                      # Folder containing source PDFs
├── vectorstore/               # Stores FAISS embeddings & index
│
├── static/                    # CSS, JS, images
├── templates/                 # HTML templates
│
└── README.md                  # Project documentation
```

---

## 💡 How It Works

1. **Document Ingestion**

   * PDFs in `/data/` are processed by `ingest.py`.
   * Texts are split and converted into vector embeddings using HuggingFace.
   * Stored locally in FAISS (`/vectorstore/`).

2. **Chatbot Query**

   * User asks a question through the Flask web interface.
   * FAISS retrieves the most relevant document chunks.
   * LangChain formats them into a context.
   * Ollama’s Mistral model generates the response.

3. **Dynamic Learning**

   * A separate Flask app (`app2.py`) lets users add new text inputs.
   * These are embedded and appended to the FAISS vector database.

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-rag-chatbot.git
cd langchain-rag-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate     # Windows
# or
source .venv/bin/activate    # Linux / Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Ollama and Mistral Model

```bash
# Download and install Ollama
https://ollama.com/download

# Once installed, pull Mistral model
ollama pull mistral
```

### 5️⃣ Ingest Your PDFs

Place your PDFs inside the `/data/` folder and run:

```bash
python ingest.py
```

### 6️⃣ Run the Chatbot

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### 7️⃣ (Optional) Run the Add-Data App

```bash
python app2.py
```

Accessible at [http://127.0.0.1:5001](http://127.0.0.1:5001)

---

## ⚡ Performance Notes

* For best speed, use **GPU embeddings** (`device='cuda'` in HuggingFace).
* Ollama automatically leverages your GPU for local inference.
* FAISS multi-threading optimized using `faiss.omp_set_num_threads(os.cpu_count())`.

---

## 🔒 Security & Privacy

All processing — from embedding to generation — happens on your **local machine**.
No data is sent to the cloud, making it ideal for **confidential or enterprise datasets**.

---

## 🧩 Future Enhancements

* Add multi-document upload and auto-refresh.
* Support for summarization and multi-turn conversations.
* Extend LLM options (e.g., `llama3`, `phi3`, `mixtral`).
* Implement persistent session memory.
* Dockerize for easy deployment.

---

## 🧑‍💻 Author

**Developed by:** [Your Name]
**LinkedIn:** [linkedin.com/in/yourprofile](#)
**GitHub:** [github.com/yourusername](#)
**Email:** [yourname@example.com](mailto:yourname@example.com)

---

## 🌟 Acknowledgements

* [LangChain](https://www.langchain.com)
* [HuggingFace](https://huggingface.co)
* [Ollama](https://ollama.com)
* [FAISS](https://github.com/facebookresearch/faiss)
