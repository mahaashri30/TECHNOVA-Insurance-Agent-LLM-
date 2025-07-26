from services.embedding_service import search

def retrieve_relevant_clauses(query: str):
    return search(query)
