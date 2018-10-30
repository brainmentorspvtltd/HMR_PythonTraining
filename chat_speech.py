import speech_recognition as sr
import webbrowser
from datetime import datetime
from gtts import gTTS
import os, random
import time
import pygame
pygame.mixer.init()

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()
device_id = None

hello_intent = ['hello','hi','hey','hi there','hie']
bye_intent = ['bye','bie','take care','see you','ttyl']
os_intent = ['calculator','notepad']

print("Welcome User".center(50))

hello_rply = "Hello, How are you ?"
bye_rply = "Bye, See you soon !!!"
counter = 0
while True:
    #user_msg = input("Enter your message : ")

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:

        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Waiting for connection")
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print("you said: " + text)

            if text in hello_intent:
                # print(hello_rply)
                tts = gTTS(text=hello_rply, lang='en')
                tts.save("hello"+str(counter)+".mp3")
                pygame.mixer.music.load('hello'+str(counter)+'.mp3')
            elif text in bye_intent:
                # print(bye_rply)
                tts = gTTS(text=bye_rply, lang='en')
                tts.save("bye"+str(counter)+".mp3")
                pygame.mixer.music.load('bye'+str(counter)+'.mp3')
            elif text.startswith("open"):
                web = text.split()[1]
                tts = gTTS(text="opening "+web, lang='en')
                tts.save("open" + str(counter) + ".mp3")
                pygame.mixer.music.load('open'+str(counter)+'.mp3')
                webbrowser.open(web+".com")
            elif text == "time please":
                currentTime = datetime.now().time()
                tts = gTTS(text=str(currentTime), lang='en')
                tts.save("time" + str(counter) + ".mp3")
                pygame.mixer.music.load('time'+str(counter)+'.mp3')
                print(currentTime)

            elif text == "play music":
                # r - raw string
                path = r"C:\Users\asus\Music"
                os.chdir(path)
                for root, folder, files in os.walk(path):
                    #print(files)
                    #for i,file in enumerate(files):
                    #     print(i,file)
                    song = random.choice(files)
                    # print(song)
                    os.startfile(song)
            else:
                print("I don't understand")

            pygame.mixer.music.play(1)
            counter += 1

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
