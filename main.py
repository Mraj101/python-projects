from types import CodeType
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys


speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
# print(voices[1].id)
speaker.setProperty('voice', voices[0].id)


def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your personal smart companion.  how may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hasnainahmedmiraj120@gmail.com', 'Ineedmoney2^100')
    server.sendmail('hasnainahmedmiraj120@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_directory = 'C:\\Users\\HP\\OneDrive\\Documents\\code\\projects-all\\pythonproject\\voice assistant'
            songs = os.listdir(music_directory)
            print(songs)    
            os.startfile(os.path.join(music_directory, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Sublime Text 3"
            code=os.listdir(codePath)
            os.startfile(os.path.join(codePath,code[12]))

        elif 'email to miraj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hasnainahmedmiraj120@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry hasnain . I am not able to send this email")
        elif 'please stop running' in query:
            speak("ok sir have a good ")
            sys.exit()