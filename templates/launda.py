import speech_recognition as nav
from win32com.client import Dispatch
from datetime import datetime
import wikipedia
import wmi
import psutil
import os
import time
import webbrowser
now = datetime.now()



dicton={'navneet':'name','yadav':'sirname','apple':'seb','mango':'am'}
fine=('fine','good','good','i am good')


def speak(audio):
    voice=Dispatch("SAPI.SpVoice")
    voice.Speak(audio)
hour = int(now.strftime("%H"))
r1=nav.Recognizer()



def time():
    a=now.strftime("%H %M")
    speak(a)
    main()
def date():
    a=now.strftime("%d %B %Y")
    speak(a)
    main()
def dictionary():
    speak("tell me what word you want to translate")
    try:
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            print(con)
            a=dicton[con.lower()]
            speak(f"{con} means {a}")
            main()
    except:
        dictionary()
def browser():
    speak("which site you want to open")
    try:
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            webbrowser.open_new_tab(f'http://www.{con}')
            speak(f"{con} opened")
            main()
    except:
        browser()
def argument():
    speak("your are a piece of shit idiot don't fuck around me")
    main()
def joke():
    speak("your life is a joke")
def music():
    speak("You dont have any songs")
def hru():
    speak("i am fine and you")
    try:
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            pro=con.lower()
            for argu in fine:
                if argu in pro:
                    speak("good to know")
                    main()
    except:
        hru()
def movie():
    speak("finding movies")
    a=r"F:\Movies\Hollywood"
    for file in os.listdir(a):
        if file.endswith(".mkv"):
            None
    os.startfile(os.path.join(a,file))
    main()
def close():
    speak("which process you want to kill")
    try:
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            c = wmi.WMI ()
            pro=con.lower()
            for process in c.Win32_Process ():
                a=str( process.Name)
                if pro in a:
                    os.system(f"TASKKILL /F /IM {pro}.exe")
        speak(f"{pro} program closed") 
        main()                  
    except Exception as e:
        close()
    
def wiki():
    speak("for whome do u want to know")
    try:
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            a=wikipedia.summary(con,sentences=2)
            speak(a)
            main()

    except Exception as e:
        wiki()
def task():
    with nav.Microphone() as listen:
        r3=nav.Recognizer()
        audio=r3.record(listen,duration=3)
        task=r3.recognize_google(audio)
def info():
    try:
        speak("do you want to know what can i do")
        with nav.Microphone() as source1:
            r2=nav.Recognizer()
            audio=r2.record(source1,duration=2)
            con=r2.recognize_google(audio)
            print(con)
            
            if con=='yes' or con=='sure' or con=='yeah' or con=='yaa':
                speak("i can do whatever you want")
                main()
            else:
                speak("okay")
                speak("so what do want to do")
                main()
    except Exception as e:
        info()    
def greet():
    if hour<12:
        speak("good morning sir")
        main()
    elif hour<18:
        speak("good afternoon,sir")
        main()
    else:
        speak("good night sir")
        main()

function={"hey dude":greet,"hey":greet,"hi":greet,"hi dude":greet,"what can you do":info,"show me your skills":info,"tell me about yourself":info,"tell me about someone":wiki,"close the program":close,"i want to see a movie":movie,"show me a movie":movie,"how are you":hru,"time":time,"what is the time":time,"tell me the time":time,"tell me the time please":time,"date":date,"what is the date":date,"tell me the date":date,"tell me the date please":date,"play music":music,"tell me a joke":joke,"hey idiot":argument,"idiot":argument,"you are idiot":argument,"you are an idiot":argument,"hey stupid":argument,"hi stupid":argument,"you are stupid":argument,"open browser":browser,"open website":browser,"translate":dictionary,"please translate":dictionary,"translate please":dictionary}
def main():
    try:
        with nav.Microphone() as source:
                r1=nav.Recognizer()
                audio=r1.record(source,duration=4)
                voice=r1.recognize_google(audio)
                starting_voice=voice.lower()
                print(starting_voice)
                for i in function:
                    a=function[starting_voice]
                    a()                 
    except Exception as e:
        main()

if __name__=='__main__':
    main()