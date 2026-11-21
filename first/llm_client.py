from groq import APIError, Groq

from config import load_api_key


def get_reply(messages) -> str:
    api_key = load_api_key()

    with Groq(api_key=api_key, timeout=30.0) as client:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=0.5,
            max_completion_tokens=2048,
            reasoning_effort="low",
            stream=False,
        )

    reply = response.choices[0].message.content

    if not reply:
        raise ValueError("Groq returned an empty response.")

    return reply


if __name__ == "__main__":
    test_messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Explain things simply.",
        },
        {
            "role": "user",
            "content": "What is an API? Explain in three short sentences.",
        },
    ]

    try:
        answer = get_reply(test_messages)
        print("Assistant:")
        print(answer)
    except (ValueError, APIError) as error:
        print(f"Request failed: {error}")
        raise SystemExit(1)