import chromadb

client = chromadb.PersistentClient(
    path="rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="nutrition_docs"
)

print("Collection Loaded")