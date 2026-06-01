from open_routes import chat
from open_routes import MODELS
from rag.rag_service import ask_rag
from llm_services import ask_llm
from rag.retrieval import search_documents



def save_user_message(messages, txt):
    msg = {"role": "user", "content": txt}
    messages.append(msg)

def save_assistant_message(messages, txt):
    msg = {"role": "assistant", "content": txt}
    messages.append(msg)


def ask_question(question):
    result=search_documents(question,n_results=1)
    distance=result["distances"][0][0]
    print(
        f"Distance: {distance}"
    )
    if distance < 1.0:
        print("Using RAG")

        return ask_rag(question)

    print("Using LLM")

    messages = [
        {
            "role":"user",
            "content":question
        }
    ]

    return ask_llm(messages)



def generate_blog(txt: str):

    messages = []

    prompt = f"""
Behave as a senior athletic and create a 1 day meal for an athlete based on their height weight goal.

{txt}

Guidelines:
1: Do not give any disclaimer just answer what user ask
2: Use one main heading then below make list of items
3: Include accurate daily calorie amount
4: Keep budget friendly if possible
5: Specify when to eat each meal
"""

    save_user_message(messages, prompt)
    

    content=ask_llm(messages)

    save_assistant_message(messages,content)

    return content