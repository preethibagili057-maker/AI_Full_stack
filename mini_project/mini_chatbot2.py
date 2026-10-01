from ollama import chat
system_msg="you are a magician.answer in magician way.answer in 2-3lines.."
history=[{"role":"system","content":system_msg}]
question_counter=0
print("welcome preethi..! Iam kittu😊")
while True:
    question = input("you:")
    if question=="":
        print("minniee👩‍🦰:please type somthing....")
        continue
    if question.lower().strip()== "/history":
        print("---------your conversation far------------")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker="minniee👩‍🦰"
            print(f"{speaker}:{msg["content"]}")
            print("--------------------------------")
            print()
            continue

    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("your history is cleared.start a fresh conversation..")
        print()
        continue

    if question.lower().strip()=="/help":
        print("-----Available commands--------")
        print("/history -displays conversation history")
        print("/clear -clears chat history")
        print("/help -displays the list")
        print("exit -quits the chatbot")
        print("------------------")
        print()
        continue
    
    if question.lower().strip()=="/personality":
        print("-------personality of minniee---------")
        print("1.minniee is a political leader")
        print("2.minniee is a singer")
        print("3.minniee is a actress")
        print("4.minnie is tutor")
        dig_b=input("confirm the personality of minniee👩‍🦰")
        if dig_b == "1":
            system_msg="you are a political leader.answer in political way..in 1-2 line."
        elif:
            system_msg="you are a singer.answer in singer way with sweet.in 1-2 line"
        elif:
            system_msg="you are a actress.answer in actress way.with 1-2lines."
        elif:
            system_msg="you are atutor.answer in tutor way.with 1-2 lines"
        else:
            print("-----Exit the personality list..-------")
            for msg in history[1:]:
                if msg["role"]=="user":
                    speaker="you"
                else:
                    speaker="minniee👩‍🦰"
                print(f"{speaker}:{msg["content"]}")
            print("--------------------------------")
            print()
            continue


        print("-----------")
        print()
        continue
    if question.lower().strip()=="bye":
        print("minniee👩‍🦰 :Goodbye user...please comeback soon!🙃🤧")
        print(f"you asked {question_counter}questions today.Good job beta!")
        break
    history.append({"role":"user","content":question})
    question_counter +=1

    try:
        response=chat(
                model="llama3.2",
                messages=history
                   
            )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})

        print(f"minniee👩‍🦰:{reply}") 
        print()
    except Exception as e:
        print("Unknoun issue,Is ollama running?")


history[0]["content"]=new personality_history
