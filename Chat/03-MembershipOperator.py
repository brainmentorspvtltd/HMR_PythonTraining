import webbrowser

hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo']
chat = True
while chat:

    usermessage = input("Enter your message : ")
    usermessage = usermessage.lower()

    #Membership Operators - in, not in
    if usermessage in hello_intent:
        print("Hi there...")
    elif usermessage.startswith('open'):
        web = usermessage.split()[1]
        webbrowser.open(web+'.com')
    elif usermessage == "bye":
        print("Bye")
        chat = False
    else:
        print("I Don't Understand")
