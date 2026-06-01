from embeddings import create_embedding

text = "Chicken breast is rich in protein"

embedding = create_embedding(text)

print(type(embedding))
print(len(embedding))

print("\nFirst 10 values:\n")

print(embedding[:10])