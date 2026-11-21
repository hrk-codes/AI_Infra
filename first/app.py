from groq import APIError

from llm_client import get_reply

def main() -> None:
    print("Ai Chat Assistant")

    user_input = input("you: ").strip()

    if not user_input:
        print("please enter a question.")
        return

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Explain things simply.",
        },
        {
            "role": "user",
            "content": user_input,
        }
    ]

    print("\nWaiting for response...")

    answer = get_reply(messages)

    print("\nAssistant:")
    print(answer)

if __name__ == "__main__":
    try:
        main()
    except (ValueError, APIError) as error:
        print(f"Request failed: {error}")
        raise SystemExit(1)
    except (KeyboardInterrupt, EOFError):
        print("\nGooodBye!")