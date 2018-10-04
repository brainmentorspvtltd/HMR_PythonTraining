chat = True
while chat:

    usermessage = input("Enter your message : ")
    usermessage = usermessage.lower()

    #Logical Operators - AND, OR, NOT
    if usermessage == 'hello' or usermessage == 'hey' or usermessage == 'hi':
        print("Hi there...")
    elif usermessage == "bye":
        print("Bye")
        chat = False
    else:
        print("I Don't Understand")
