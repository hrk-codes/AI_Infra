from groq import APIError

from llm_client import get_reply
from memory.chat_memory import create_memory, add_exchange, clear_memory

def main() -> None:

    messages = create_memory()

    print("Ai Chat Assistant")

    print("commands: /exit to quit, /clear to forget the conversation.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "/exit":
            print("GoodBye!")
            break

        if user_input.lower() == "/clear":
            clear_memory(messages)
            print("Conversation cleared.")
            continue

        if not user_input:
            continue

        user_message = {
            "role": "user",
            "content": user_input,
        }

        request_messages = messages + [user_message]

        print("\nWaiting for response...")

        try:
            answer = get_reply(request_messages)
        except(ValueError, APIError) as error:
            print(f"Request failed: {error}")
            continue

        print(f'\nassistant: {answer}')

        add_exchange(messages, user_input, answer)
        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")