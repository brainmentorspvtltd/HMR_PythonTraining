import webbrowser
from datetime import datetime
import os, random

hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo']
date_intent = ['tell me date','date please', 'date', 'show me date']
time_intent = ['tell me time','time please', 'time', 'show me time']
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
    elif usermessage in time_intent:
        curr_time = datetime.now().time()
        print("Current time is",curr_time)
    elif usermessage in date_intent:
        curr_date = datetime.now().date()
        print("Today's date is",curr_date)
    elif usermessage == "play music":
        path = r'C:\Users\asus\Music'
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif usermessage == "bye":
        print("Bye")
        chat = False
    else:
        print("I Don't Understand")
