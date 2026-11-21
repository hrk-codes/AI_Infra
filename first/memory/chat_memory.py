def create_memory():
    return [
        {
            "role": "system",
            "content": "You are a helpful assistant. Explain things simply.",
        }
    ]
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