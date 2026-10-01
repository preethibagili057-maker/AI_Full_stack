from ollama import chat
system_msg="you are a singer.answer in singer way."
while True:
    question = input("you:")
    if question=="":
        print("preethi👩‍🦰:type somthing....")
    if question.lower().strip()== "exit":
        print("preethi👩‍🦰 :Goodbye user...please comeback soon!🙃🤧")
        break

    try:
        response=chat(
                model="llama3.2",
                messages=[
                    {
                        "role":"system",
                        "content":system_msg
                    },
                    {
                        "role":"user",
                        "content":question
                    }
                ]
        )
        print(f"Preethi 😘:{response.message.content}") 
        print()
    except Exception as e:
        print("Unknoun issue,Is ollama running?")