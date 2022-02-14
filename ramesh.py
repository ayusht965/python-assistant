import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the time is")
    speak(Time)


def date():
    year= int( datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    Curdate= int (datetime.datetime.now().day)
    speak("the current date is")
    speak(Curdate)
    speak(month) 
    speak(year)
 
def wishme():
    speak(" hey Welcome back Ayush")
    hour=int( datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening")
    else:
        speak("good night")
    
    speak("how may i help you sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio= r.listen(source)

    try: 
        print("Rcognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please..")

        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\python\jarvis\ss\ss.png")

def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery
    speak("battery is at" + battery.percent)
def jokes():
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishme()

    while True:
        query= takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date() 

        elif "wikipedia" in query:
            query= query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=2)
            speak("searching...")
            speak(result)

        elif "chrome" in query:
            speak("What should i search")
            chromepath= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.open("www.google.com/search?q="+search)

        elif 'offline'or'band hoja' in query:
            quit() 

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir= "E:\music"
            songs= os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak('what should i remember')
            data = takeCommand()
            speak(" you said me to remember" + data)
            remember= open("data.txt" , "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember= open("data.txt", "r")
            speak("you said me to remember "+ remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("the screenshot has been taken")
        elif "cpu" in query:
            cpu() 
        elif "joke" in query:
            jokes()