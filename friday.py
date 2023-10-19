import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Friday, Your Personal Assistant. Please tell me how can I help you.")  

def close_music():
    os.system('taskkill /IM chrome.exe /F')
    close_music()     

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
    server.login('Your email id', 'your email password here')
    server.sendmail('your email id', to, content)
    server.close()

def stop_music():
    os.system('taskkill /IM vlc.exe /F')
    stop_music()

def close_edge():
    os.system('taskkill /IM msedge.exe /F')
    close_edge()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        if 'search' in query:
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

        elif 'my name is' in query:
            name = query.replace('my name is', '')
            speak('hello ' + name)
            speak('you got such a beautiful name.')
            speak('that is great to talk with you.')

        elif 'play my music' in query:
            music_dir = 'location of your music folder' #Enter the location of your music directory here
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play my song' in query:
            music_dir = 'location of your music folder' #Again enter the location of your music directory here
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[16]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}, I hope everything is going great today")

        elif 'what is the date' in query:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            message = "Today's date is " + current_date
            speak(message)
            speak('Hope you are doing great today')

        elif 'open vs code' in query:
            codePath = "location of your vs code" #Enter the location of your vs code here 
            os.startfile(codePath)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'hello' in query:
            speak('Hello!Hope you are good. What can i do for you?')

        elif 'hi' in query:
            speak('Hello!Hope you are good. What can i do for you?')

        elif 'how are you' in query:
            speak('I am fine. Thank you for asking.')

        elif 'how r u' in query:
            speak('I am fine. Thank you for asking.')

        elif 'open notepad' in query:
            notepad = "location of notepad" #Enter the location of your notepad here
            os.startfile(notepad)

        elif 'open discord' in query:
            discord = "location of discord" #Enter the location of discord if you have
            os.startfile(discord)

        elif 'open file manager' in query:
            manager = "location of this pc" #Enter the location of this pc here
            os.startfile(manager)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'will you marry me' in query:
            speak('i did not think about it yet, because I have other works to do.')
            speak('But I think I will become your best friend, if you want to.')

        elif 'what is your name' in query:
            speak('My name is Friday.')
            speak('And I am your personal assistant.')

        elif 'who is your best friend' in query:
            speak('You are my best friend.')

        elif 'do you like me' in query:
            speak('I like you.')
            speak('But as a best friend, Hope you understand what I mean.')

        elif 'stop music' in query:
            stop_music()

        elif 'close music' in query:
            close_music()  

        elif 'close edge' in query:
            close_edge()

        elif 'send email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ("your email id")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am really Sorry, But I am not able to send this email")

        elif 'goodbye' in query:
            speak('Goodbye!! See you soon.')
            break
