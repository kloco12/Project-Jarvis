#Imports
import webbrowser
import speech_recognition as sp
from datetime import datetime
import pyttsx3
import time
import os
import random
import sys

rec = sp.Recognizer()
jarvis = pyttsx3.init()
now = datetime.now()
current_time = now.strftime("%H:%M")
voices = jarvis.getProperty('voices')
myMicro = sp.Microphone(device_index=1)

x = 1

while x != 3:
    x = x + 1
    print("""

                                    ░░░░░██╗░█████╗░██████╗░██╗░░░██╗██╗░██████╗
                                    ░░░░░██║██╔══██╗██╔══██╗██║░░░██║██║██╔════╝
                                    ░░░░░██║███████║██████╔╝╚██╗░██╔╝██║╚█████╗░
                                    ██╗░░██║██╔══██║██╔══██╗░╚████╔╝░██║░╚═══██╗
                                    ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║██████╔╝
                                    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░

                                            █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀
                                            █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█  ▄
            """)
    time.sleep(1)
    os.system("cls")
    print("""

                                    ░░░░░██╗░█████╗░██████╗░██╗░░░██╗██╗░██████╗
                                    ░░░░░██║██╔══██╗██╔══██╗██║░░░██║██║██╔════╝
                                    ░░░░░██║███████║██████╔╝╚██╗░██╔╝██║╚█████╗░
                                    ██╗░░██║██╔══██║██╔══██╗░╚████╔╝░██║░╚═══██╗
                                    ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║██████╔╝
                                    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░

                                            █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀
                                            █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█  ▄ ▄ 
    """)
    time.sleep(1)
    os.system("cls")    
    print("""

                                    ░░░░░██╗░█████╗░██████╗░██╗░░░██╗██╗░██████╗
                                    ░░░░░██║██╔══██╗██╔══██╗██║░░░██║██║██╔════╝
                                    ░░░░░██║███████║██████╔╝╚██╗░██╔╝██║╚█████╗░
                                    ██╗░░██║██╔══██║██╔══██╗░╚████╔╝░██║░╚═══██╗
                                    ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║██████╔╝
                                    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░

                                            █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀
                                            █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█  ▄ ▄ ▄
    """)
    time.sleep(1)
    os.system("cls") 

os.system("cls")

print("What is your name?")
jarvis.say("what is your name")
jarvis.runAndWait()
name = input("Enter Here: ")
os.system("cls")

print("Microphone (Early Developement (BETAv1.0.0))\nNon Microphone (Version 1.2.0)")
jarvis.say("Which version do you want?")
jarvis.runAndWait()
switch = input("\nWhich version do you want?\n(NM or Non Microphone / M or Microphone / Help /): ")

if switch == "NM" or switch == "nm" or switch == "Nm" or switch == "nM" or switch == "Non Microphone" or switch == "non Microphone" or switch == "Non microphone":
    os.system("cls")
    jarvis = pyttsx3.init()
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    voices = jarvis.getProperty('voices')

    #Voice changer
    jarvis.setProperty('rate', 230)
    jarvis.setProperty('volume', 0.9)

    os.system("cls")
    #-------------------------------------------------------------Main AI----------------------------------------------------------------

    print("Hi, I'm Jarvis, your virtual assistant\nHow Can i help you")
    jarvis.say("Hi, I'm Jarvis, your virtual assistant, how can i help you")
    jarvis.runAndWait()

    while True:
        os.system("cls")
        ci = 0
        ci = input(name+"(you): ")

        if ci == "tell me a joke" or ci == "tell me a joke":
            jokemaker = [
                "I got million joke to tell you",
                "Trust me this is going to make you laugh",
                "Ok Jarvis joke mode is on",
            ]
            jokemaker2 = random.choice(jokemaker)
            print("\n"+jokemaker2)
            jarvis.say("bim, "+jokemaker2)
            time.sleep(0.4)

            actualjoke = [
                "What’s the smartest insect? A spelling bee!",
                "How does the ocean say hi? It waves!",
                "Name the kind of tree you can hold in your hand? A palm tree!",
                "Where did the music teacher leave her keys? In the piano!",
                ]

            actualjoke2 = random.choice(actualjoke)
            print(actualjoke2)
            jarvis.say(actualjoke2)
            jarvis.runAndWait()
    
        elif ci == "what is your name" or ci == "who are you":
            print("My Name Is J.A.R.V.I.S but but i shortened it to Jarvis")
            jarvis.say("My Name Is Jarvis but but i shortened it to That")
            jarvis.runAndWait()
    
        elif ci == "open google" or ci == "open google.com":
            print("Opening Now")
            jarvis.say("opening now")
            jarvis.runAndWait()
            webbrowser.open_new("https://www.google.com")

        elif ci == "open a website":
            print("Please write the URL below")
            jarvis.say("please write the url below")
            jarvis.runAndWait()
            url = input("Enter Here: ")
            os.system("cls")
            print("Opening Now")
            jarvis.say("opening now")
            jarvis.runAndWait()
            webbrowser.open_new(url)
    
        elif ci == "rename" or ci == "change my name":
            print("What Do you want to change it into")
            jarvis.say("What Do you want to change it into")
            jarvis.runAndWait()
            name = input("Write Here: ")
            os.system("cls")
            print("Your name is now changed!")
            jarvis.say("Your name is now changed!")
            jarvis.runAndWait()
    
        elif ci == "nice":
            print("Well, Good to know")
            jarvis.say("Well, Good to know")
            jarvis.runAndWait()

        elif ci == "Good" or ci == "good":
            print("well thats good to know")
            jarvis.say("b, Well thats good to know")
            jarvis.runAndWait()

        elif ci == "how are you" or ci == "How are you":
            treat = [
                "Hello, I'm fine thanks",
                "I'm pretty good, thanks",
                "I'm happy to be here",
                "I'm Good, what about you",
            ]
            treat2 = random.choice(treat)
            print(treat2)
            jarvis.say(treat2)
            jarvis.runAndWait()
    
        elif ci == "time" or ci == "what is the time":
            print("The Time now in your region is ", current_time)
            jarvis.say("The Time now in your region is ", current_time)
            jarvis.runAndWait()
    
        elif ci == "are you alright" or ci == "are you fine":
            print("Im Fine, Thanks For Asking")
            jarvis.say("Im Fine, Thanks for Asking")
            jarvis.runAndWait()

        elif ci == "hey jarvis":
            hj = [
                "I'm here",
                "Go Ahead...",
                "Hello how can i help",
                "Is there anything that i can do for you",
            ]
            hj2 = random.choice(hj)
            print(hj2)
            jarvis.say("b, "+hj2)
            jarvis.runAndWait()
    
        elif ci == "":
            print("Please write something valid")
            jarvis.say("Please write something valid")
            jarvis.runAndWait()

        elif ci == "order products from amazon" or ci == "order products from ebay":
            print("This Feture is Coming Soon")
            jarvis.say("This Feture is Coming Soon")
            jarvis.runAndWait()
    
        elif ci == "hi" or ci == "Hi" or ci == "Hello" or ci == "hello":
            greet = [
                "Go Ahead",
                "Hi",
                "Im here",
                "Jarvis here. Let me know if i can help",
            ]
            greet2 = random.choice(greet)
            print(greet2)
            jarvis.say(greet2)
            jarvis.runAndWait()


        else:
            idk = [
                "Im not sure if I Understand?",
                "I did not get that correctly?",
                "I dont know what that means?",
                "Go On",
            ]

            idk2 = random.choice(idk)
            print(idk2)
            jarvis.say(idk2)
            jarvis.runAndWait()

elif switch == "M" or switch == "m" or switch == "Microphone" or switch == "microphone":
    os.system("cls")
    print("Hi "+name+", I'm Jarvis, your virtual assistant\nHow Can i help you")
    jarvis.say("Hi "+name+", I'm Jarvis, your virtual assistant, how can i help you")
    jarvis.runAndWait()

    while True:
        os.system("cls")
        with myMicro as source:
            print("Hi "+name+", Im Listening...")
            jarvis.say("I'm Listening.")
            jarvis.runAndWait()
            audio = rec.listen(source)
            ci = rec.recognize_google(audio)

            if ci == "tell me a joke" or ci == "tell me a joke":
                jokemaker = [
                "I got million joke to tell you",
                "Trust me this is going to make you laugh",
                "Ok Jarvis joke mode is on",
            ]
                jokemaker2 = random.choice(jokemaker)
                print("\n"+jokemaker2)
                jarvis.say(jokemaker2)
                time.sleep(0.4)

                actualjoke = [
                    "What’s the smartest insect? A spelling bee!",
                    "How does the ocean say hi? It waves!",
                    "Name the kind of tree you can hold in your hand? A palm tree!",
                    "Where did the music teacher leave her keys? In the piano!",
                    ]

                actualjoke2 = random.choice(actualjoke)
                print(actualjoke2)
                jarvis.say(actualjoke2)
                jarvis.runAndWait()
        

            elif ci == "good" or ci == "im fine" or ci == "im doing well" or ci == "im very good" or ci == "im good":
                print("well thats good to know")
                jarvis.say("Well thats good to know")
                jarvis.runAndWait()
            
            elif ci == "are you alright" or ci == "are you good" or ci == "how are you feeling?" or ci == "how are you today" or ci == "how are you":
                print("Im Fine, Thanks For Asking")
                jarvis.say("Im Fine, Thanks for Asking")
                jarvis.runAndWait()
            
            elif ci == "open google" or ci == "open google.com" or ci == "open chrome" or ci == "open browser":
                print("Opening Now")
                jarvis.say("opening now")
                jarvis.runAndWait()
                webbrowser.open_new("https://www.google.com")

            elif ci == "open a website":
                print("Please write the URL below")
                jarvis.say("please write the url below")
                jarvis.runAndWait()
                url = input("Enter Here: ")
                os.system("cls")
                print("Opening Now")
                jarvis.say("opening now")
                jarvis.runAndWait()
                webbrowser.open_new(url)

            elif ci == "how are you" or ci == "How are you" or ci == "how are you feeling?":
                treat = [
                    "Hello, I'm fine thanks",
                    "I'm pretty good, thanks",
                    "I'm happy to be here",
                    "I'm Good, what about you",
                ]
                treat2 = random.choice(treat)
                print(treat2)
                jarvis.say(treat2)
                jarvis.runAndWait()
        
            elif ci == "time" or ci == "what is the time" or ci== "what time is it":
                print("The Time now in your region is ", current_time)
                jarvis.say("The Time now in your region is ", current_time)
                jarvis.runAndWait()

            elif ci == "what is your name" or ci == "who are you":
                print("My Name Is J.A.R.V.I.S but i shortened it to Jarvis")
                jarvis.say("My Name Stands for many things but I shortened it to Jarvis")
                jarvis.runAndWait()
            
            elif ci == "how old are you" or ci == "what is your age":
                print("Im afraid i dont have an age")
                jarvis.say("Im afraid i dont have an age")
                jarvis.runAndWait()

            elif ci == "nice":
                print("Well, Good to know")
                jarvis.say("Well, Good to know")
                jarvis.runAndWait()

            elif ci == "hey jarvis":
                hj = [
                    "I'm here",
                    "Go Ahead...",
                    "Hello how can i help",
                    "Is there anything that i can do for you",
                ]
                hj2 = random.choice(hj)
                print(hj2)
                jarvis.say(hj2)
                jarvis.runAndWait()
        
            elif ci == "":
                print("Please say something valid")
                jarvis.say("Please say something valid")
                jarvis.runAndWait()

            elif ci == "order products from amazon" or ci == "order products from ebay" or ci == "open amazon" or ci == "open ebay":
                print("This Feture is Coming Soon")
                jarvis.say("This Feture is Coming Soon")
                jarvis.runAndWait()
        
            elif ci == "hi" or ci == "Hi" or ci == "Hello" or ci == "hello" or ci == "hiya" or ci == "hi jarvis" or ci == "jarvis":
                greet = [
                    "Go Ahead",
                    "Hi",
                    "Im here",
                    "Jarvis here. Let me know if i can help",
                ]
                greet2 = random.choice(greet)
                print(greet2)
                jarvis.say(greet2)
                jarvis.runAndWait()
            
            elif ci == "rename" or ci == "change my name":
                print("What Do you want to change it into")
                jarvis.say("What Do you want to change it into")
                jarvis.runAndWait()
                name = input("Write Here: ")
                os.system("cls")
                print("Your name is now changed!")
                jarvis.say("Your name is now changed!")
                jarvis.runAndWait()


            else:
                idk = [
                    "Im not sure if I Understand?",
                    "I did not get that correctly?",
                    "I dont know what that means?",
                ]   
                idk2 = random.choice(idk)
                print(idk2)
                jarvis.say(idk2)
                jarvis.runAndWait()

elif switch == "help" or switch == "Help" or switch == "H" or switch == "h":
    print("Coming Soon")
    jarvis.say("Coming soon.")
    jarvis.runAndWait()