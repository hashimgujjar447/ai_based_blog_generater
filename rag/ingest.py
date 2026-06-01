from chunker import chunk_text
from embeddings import create_embedding
from vector_store import collection

with open(
    "rag/data/nutritions.txt",
    "r",
    encoding="utf-8"
) as file:

    text = file.read()

chunks = chunk_text(text)

for index, chunk in enumerate(chunks):

    embedding = create_embedding(chunk)

    collection.add(
        ids=[str(index)],
        documents=[chunk],
        embeddings=[embedding]
    )

print(f"{len(chunks)} chunks stored successfully.")