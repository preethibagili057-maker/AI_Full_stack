from ollama import chat

messages=[
    {"role":"system","content":"identify sentiment as positivve,negative,neutral.Replay with one word only."},
    {"role":"user","content":"great movie."},
    {"role":"system","content":"positive"},
    {"role":"user","content":"waste of money."},
    {"role":"system","content":"negative"},
    {"role":"user","content":"it is okey"},
     {"role":"system","content":"neutral."},
    {"role":"user","content":"loved the acting but the ending was dull.."}
]
response = chat(
    model="llama3.2",
    messages=messages
)
print(response.message.content)