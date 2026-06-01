from chunker import chunk_text

with open(
    "rag/data/nutritions.txt",
    "r",
    encoding="utf-8"
) as file:

    text = file.read()

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"\n------ CHUNK {i+1} ------\n")
    print(chunk)