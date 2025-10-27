import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from filelock import FileLock

DB_FAISS_PATH = 'vectorstore/db_faiss_1'
_LOCK = FileLock(DB_FAISS_PATH + ".lock")

def add_user_input_to_db(user_input: str) -> int:
    try:
        # 1) Embeddings (must match the model used to build the index)
        embeddings = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-MiniLM-L6-v2',
            model_kwargs={'device': 'cuda'}
        )

        # 2) Load, add text, save — under a lock to avoid corruption
        with _LOCK:
            db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
            db.add_texts([user_input])
            db.save_local(DB_FAISS_PATH)

        return 1
    except Exception as e:
        # Optional: log e for debugging
        print("add_user_input_to_db error:", e)
        return 0

if __name__ == "__main__":
    # Example user input
    user_input = "This is an example sentence."

    # Add user input to the vector database
    add_user_input_to_db(user_input)
