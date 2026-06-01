from rag.retrieval import search_documents
from open_routes import chat
from llm_services import ask_llm

def ask_rag(question):
    results=search_documents(question)

    context="\n".join(results["documents"][0])
    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:

"I could not find that information in the provided document."

Context:
{context}

Question:
{question}
"""
    
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]

   

    return ask_llm(messages)
    
