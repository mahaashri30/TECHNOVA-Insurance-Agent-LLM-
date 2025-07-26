from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

# Create FAISS index
dimension = 384  # Model output size
index = faiss.IndexFlatL2(dimension)

# In-memory storage (can persist later)
documents = []

def process_document(filename: str, text: str):
    global documents, index
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings, dtype='float32'))

    for chunk in chunks:
        documents.append({"source": filename, "text": chunk})

def search(query: str, top_k: int = 3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector, dtype='float32'), top_k)
    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])
    return results
