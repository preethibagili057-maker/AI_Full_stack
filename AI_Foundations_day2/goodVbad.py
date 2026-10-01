from ollama import chat

bad="Tell me about dogs.."
good="list 3 dog breeds that are suitable for penthouse.2 lines about each.."

response1=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":bad
        }
    ]
)
response2=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":good
        }
    ]
)

print(f"bad prompt result:{response1.message.content}")

print()

print(f"good prompt result:{response2.message.content}")