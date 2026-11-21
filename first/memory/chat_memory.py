import json
from datetime import datetime
from pathlib import Path

HISTORY_PATH = Path(__file__).resolve().parent.parent / "history.json"

def create_memory():
    return [
        {
            "role": "system",
            "content": "You are a helpful assistant. Explain things simply.",
        }
    ]

def load_memory():
    try:
        history = json.loads(HISTORY_PATH.read_text(encoding="utf-8"))

        if not isinstance(history, list) or len(history) % 2 != 0:
            raise ValueError("Invalid conversation history.")

        for index, message in enumerate(history):
            expected_role = "user" if index % 2 == 0 else "assistant"

            if (
                not isinstance(message, dict)
                or set(message) != {"role", "content"}
                or message["role"] != expected_role
                or not isinstance(message["content"], str)
                or not message["content"].strip()
            ):
                raise ValueError("Invalid conversation message.")

    except FileNotFoundError:
        return create_memory(), ""

    except ValueError:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup_path = HISTORY_PATH.with_name(
            f"history.corrupt-{timestamp}.json"
        )
        HISTORY_PATH.rename(backup_path)

        return (
            create_memory(),
            f"Invalid history preserved in {backup_path.name}. Starting fresh.",
        )

    return create_memory() + history, ""


def save_memory(messages):
    temporary_path = HISTORY_PATH.with_name("history.json.tmp")

    temporary_path.write_text(
        json.dumps(messages[1:], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    temporary_path.replace(HISTORY_PATH)
def add_exchange(messages, user_input, answer):
    messages.extend(
        [
            {
                "role": "user",
                "content": user_input,
            },
            {
                "role": "assistant",
                "content": answer,
            },
        ]
    )

def clear_memory(messages):
    messages.clear()
    messages.extend(create_memory())