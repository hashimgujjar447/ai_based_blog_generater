import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))
from embeddings import create_embedding
from vector_store import collection
from open_routes import chat
query = "What is Hashim's secret protein food?"




query_embedding = create_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)


context="\n".join(results["documents"][0])

print(context)


prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""
print(prompt)

messages=[{"role":"user","content":prompt}]


response = chat(
    messages,
    "openai/gpt-oss-20b:free"
)

print(response["choices"][0]["message"]["content"])