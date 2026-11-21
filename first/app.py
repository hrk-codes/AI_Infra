from groq import APIError

from llm_client import get_reply

from memory.chat_memory import(
    load_memory,
    save_memory,
    add_exchange,
    clear_memory,
)
def main() -> None:
    try:
        messages, notice = load_memory()
    except OSError as error:
        print(f"could not load or preserve history: {error}")
        return

    print("Ai Chat Assistant")

    print("commands: /exit to quit, /clear to forget the conversation.")

    if notice:
        print(notice)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "/exit":
            print("GoodBye!")
            break

        if user_input.lower() == "/clear":
            try:
                clear_memory(messages)
                print("Active and saved conversation cleared.")
            except OSError as error:
                print(f"Could not clear saved history: {error}")
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

        try:
            save_memory(messages)
        except OSError as error:
            print(f"Reply received, but history could not be saved: {error}")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")