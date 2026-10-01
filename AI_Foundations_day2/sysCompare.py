from ollama import chat
 
roles=[
    "You are a strict math teacher.Answer briskly and within 1 line",
    "you are a movie actor.Answer in a filmy way.1 line answer",
    "you are a lawyer.ANswer professionally.1 line answer"
]

for role in roles:
    response=chat(
        model="llama3.2",
        messages=[
            {
                "role":"system",
                "content":role
            },
            {
                "role":"user",
                "content":"How many colours in the rainbow?"    
            }
        ]

    )
print(f"---{role}---")
print(response.message.content)
print()