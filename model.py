import os
from pathlib import Path

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

DB_FAISS_PATH = "vectorstore/db_faiss_1"

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Question:
{question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    # Variables must be "context" and "question"
    return PromptTemplate(
        template=custom_prompt_template,
        input_variables=["context", "question"],
    )

# ---- singletons ----
# Reuse one GPU embedding model (fast + matches your FAISS index)
_EMB = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"},
)

def _load_db():
    db_dir = Path(DB_FAISS_PATH)
    if not db_dir.exists():
        raise RuntimeError(
            f"Vector store not found at '{DB_FAISS_PATH}'. Run ingest.py first to build the index."
        )
    # IMPORTANT: pass the same embeddings object used to build it
    return FAISS.load_local(DB_FAISS_PATH, _EMB, allow_dangerous_deserialization=True)

def load_llm():
    # Ensure: ollama pull mistral  (and service is running)
    return Ollama(
        model="mistral",  # "mistral:latest" also fine
        base_url=os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
        temperature=0.2,
        num_ctx=4096,
    )

def _format_docs(docs):
    # Join retrieved docs into a single context string
    return "\n\n".join(d.page_content for d in docs)

def build_rag_chain():
    db = _load_db()
    retriever = db.as_retriever(search_kwargs={"k": 3})
    prompt = set_custom_prompt()
    llm = load_llm()

    # LCEL pipeline:
    # input -> {"context": retriever(input) |> format, "question": input} -> prompt -> llm -> str
    chain = {
        "context": retriever | RunnableLambda(_format_docs),
        "question": RunnablePassthrough(),
    } | prompt | llm | StrOutputParser()

    return chain

# ---- public API (sync, Flask-friendly) ----
def final_result(query: str) -> str:
    try:
        chain = build_rag_chain()
        answer = chain.invoke(query)  # returns a string via StrOutputParser
        return answer
    except Exception as e:
        return f"An error occurred from final result function : {e}"
