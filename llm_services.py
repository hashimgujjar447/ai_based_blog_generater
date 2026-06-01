from open_routes import MODELS,chat

def ask_llm(messages):

    for model in MODELS:

        try:

            print(f"Trying model: {model}")

            response = chat(messages, model)

            if "error" in response:
                print(f"{model} error: {response['error']['message']}")
                continue

            if "choices" in response:

                print(f"Success with: {model}")

                return response["choices"][0]["message"]["content"]

        except Exception as e:

            print(f"{model} failed: {e}")

            continue

    return "All models failed"