from rag.embeddings import create_embedding
from rag.vector_store import collection

def search_documents(query,n_results=5):

    query_embedding=create_embedding(query)

    results=collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )


    return results
