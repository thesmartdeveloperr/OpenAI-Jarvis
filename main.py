import speech_recognition as sr
import os
import webbrowser
import openai


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred"

if __name__=='__main__':
    print('hello')
    say("Hello i am an AI")
    while True:
        print("listening...")
        query=takeCommand()
        
        sites=[["youtube","https://www.youtube.com/"],
               ["google","https://www.google.com/"],
               ["wikipedia","https://www.wikipedia.org/"],
               ["amazon","https://www.amazon.in/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if "play music" in query.lower():
            musicPath="/users/dhruvbansal/downloads/downfall.mp3"
            os.system(f"open {musicPath}")

        # say(query)
