# from types import CodeType
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import PyPDF2


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

    speak("I am your personal smart companion TOM.  how may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=250
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
    server.login('hasnainahmedmiraj120@gmail.com', '00')
    server.sendmail('hasnainahmedmiraj120@gmail.com', content)
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
        elif 'hello' in query:
            speak("hi")
        elif "how are you" in query:
            speak('I am fine, what about you')
        elif "name" in query:
            speak("My name is TOM")
        elif "who is your master" in query:
            speak("My master is hasnain ahmed miraj")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'what can you do' in query:
            speak('I can do tasks for you. Most important thing is I can tell jokes,ha ha ha')
        elif 'tell me a joke' in query:
            speak('')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_directory = 'C:\\Users\\HP\\OneDrive\\Documents\\code\\projects-all\\pythonproject\\voice assistant'
            songs = os.listdir(music_directory)
            print(songs)    
            os.startfile(os.path.join(music_directory, songs[1]))

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
                to = "mrajhasnain101@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry hasnain . I am not able to send this email")
        elif 'read book' in query:
            book=open('Understanding_Software_Architecture.pdf','rb') 
                                                                    #give the name of the pdf file and keep it in the directory where you main.py is
            pdf_reader=PyPDF2.PdfFileReader(book) 
                                                #use PyPDF2.PdfFileReader() to select the book varible
            total_page=pdf_reader.numPages # .numPages method is used from 
                                        #PyPdf2   to which returns the total number of pages 
                                    #here we initilize the python text to speech module
            startpage=10 #initializing the page from where we can start to listen to
            for i in range(startpage,total_page): #iterating everytime whenever a page ends
                page=pdf_reader.getPage(i)
                                            #selecting a single page from pdf and iterating everytime with (i)
                text=page.extract_text()   #extracting the text of the page
                speak("ok here is how it goes.......")
                speak(text)           #spaker will say the extrancted text only
                      
                                  

        elif 'exit' in query:
            speak("ok sir have a good time")
            sys.exit()