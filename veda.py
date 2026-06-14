import ollama

def ask_ai(question):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': question
            }
        ]
    )
    return response['message']['content']


def gym_trainer(question):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'system',
                'content': """
You are a gym trainer.

Rules:
- Be polite and friendly
- Keep answers short and to the point
- Give diet plans for weight loss when asked
"""
            },
            {
                'role': 'user',
                'content': question
            }
        ]
    )
    return response['message']['content']


print("=== AI Assistant Chatbot ===")
print("1. General AI")
print("2. Gym Trainer")

choice = input("Choose an option (v3da or v3da gym mode): ")

while True:
    question = input("\nAsk a question (or type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if choice == "v3da":
        print("\nAI:", ask_ai(question))

    elif choice == "veda gym mode":
        print("\nGym Trainer:", gym_trainer(question))

    else:
        print("Invalid choice.")
        break
