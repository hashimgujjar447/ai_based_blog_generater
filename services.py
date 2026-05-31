from open_routes import chat
from open_routes import MODELS

messages = []

def save_user_message(messages, txt):
    msg = {"role": "user", "content": txt}
    messages.append(msg)

def save_assistant_message(messages, txt):
    msg = {"role": "assistant", "content": txt}
    messages.append(msg)

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

    for model in MODELS:

        try:
            print(f"Trying model: {model}")

            response = chat(messages, model)

            if "error" in response:
                print(f"{model} error: {response['error']['message']}")
                continue

            if "choices" in response:

                content = response["choices"][0]["message"]["content"]

                save_assistant_message(messages, content)

                print(f"Success with: {model}")

                return content

        except Exception as e:
            print(f"{model} failed: {str(e)}")
            continue

    return "All models failed"