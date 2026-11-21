from groq import APIError

from llm_client import get_reply

def main() -> None:

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Explain things simply.",
        }
    ]

    print("Ai Chat Assistant")

    print("Type /exit to quit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "/exit":
            print("GoodBye!")
            break

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


        messages.extend(
            [
                user_message,
                {
                    "role": "assistant",
                    "content": answer,
                },
            ]
        )
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")