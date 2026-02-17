messages = [
    "Hi",
    "",
    "Hello",
    "Hi",
    "  ",
    "How are you?",
    "Hello"
]
seen = set()
cleaned_messages = []
for msg in messages:
    msg = msg.strip()     
    if msg and msg not in seen:
        cleaned_messages.append(msg)
        seen.add(msg)
print(cleaned_messages)