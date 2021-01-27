import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import email
import smtplib
import pafy
import vlc

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi! I am Jarvis sir. Please tell me how I can help you?")

def takeCommand():
    # Uzima mikrofon input Korisnika i vraca string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print("User said:",query)

        except Exception as e:
            print(e)

            print("Say that again please...")
            return "None"

    return query

def sendEmail(do,content):
    server = smtplib.SMTP('smtp.gmail.com',587) # host
    server.ehlo()
    server.starttls()
    server.login('viktor08mivanovic@gmail.com','viktor08+-')
    server.sendmail('viktor08mivanovic@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
   # wishMe()
    while True:
        query = takeCommand().lower()

        # Logika za izvrsavanje zasnovana na query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("Accounting to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            speak("You asked about time")
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {str_time}/n")
            print(str_time)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
            """url = "https://www.youtube.com/watch?v=gl1aHhXnN1k"
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()"""

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open code' in query:
            codePath = "D:\\Visual Studio Code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open visual' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)
        elif 'email to victor' in query:
            #speak("Send email to whom Sir?")
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "viktoivanovic.stadion@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. Unable to send email. Try again please!")

