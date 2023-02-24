import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import webbrowser
import api
import emotion_detection as ed
import pyjokes as pj
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=30, phrase_time_limit=7)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"query: {query}")

    except Exception as e:
        print('Sorry, say that again please...')
        return "none"
    query = query.lower()
    return query

def greet():
    hh = int(datetime.datetime.now().hour)

    if hh >=0 and hh < 12:
        speak('Good morning sir')
    elif hh >= 12 and hh < 18:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')
    speak("I'm Marc, your personal recommendation system.")

def recommendation(emotion):
    while True:
        
        if 'happy' in emotion:
            print('---')
            speak('Sir, here are some happy genre songs')
            print('---')
            api.happy()
            print('---')
            break

        elif 'sad' in emotion:
            print('---')
            speak('Sir, here are some heart break songs')
            print('---')
            api.sad()
            print('---')
            break

        elif 'fear' in emotion:
            print('---')
            speak('Sir, you are looking afraid. What happened?')
            statement = command().lower()
            if 'yes' in statement:
                speak('Should I call 911?')
                user = command().lower()
                if 'no' in user:
                    break
                else:
                    speak('Calling 911')
            else:
                speak('Then I think I detected it wrong.')
            break

        elif 'disgust' in emotion:
            print('---')
            speak('Sir, I am also feeling disgusted.')
            break
            
        elif 'angry' in emotion:
            print('---')
            speak('Why are you angry sir. Did I do something wrong?')
            statement = command().lower()
            if 'no' in statement:
                speak('Then should I change your mood?')
                user = command().lower()
                if 'ok' in user or 'yes' in user:
                    speak('Get ready for some chuckles')
                    joke = pj.get_joke(language='en', category='neutral')
                    speak(joke)
                else:
                    break
            else:
                speak('I am sorry sir. I will not repeat that again.')
            break

        elif 'neutral' in emotion:
            print('---')
            speak('Sir, you are looking dull. Here are some chill beats.')
            print('---')
            api.neutral()
            print('---')
            break

        elif 'surprise' in emotion:
            speak('You are looking surprised sir. What happened?')
            statement = command().lower()
            if 'nothing' in statement or 'no' in statement:
                speak('Then should I suggest some songs sir?')
                user = command().lower()
                if 'yes' in user:
                    speak('Sir, here are some songs for you.')
                    print('---')
                    api.neutral()
                    print('---')
                else:
                    break
            else:
                speak('OK sir')
                break
        
        else:
            speak('No feelings detected.')
            speak('You can tell me what to search. Just call me.')
            break

def assist():
    while True:
        query = command()

        if 'open notepad' in query:
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)
            break

        elif 'Google' in query:
            speak('Sir, what should I search?')
            ques = command().lower()
            webbrowser.open(f"{ques}")
            break

        elif 'search' in query or 'song' in query:
            speak('Sir, which song should I search?')
            ques = command().lower()
            speak('Sir, here are some results')
            print('---')
            api.search(f"{ques}")
            print('---')
            break

        elif 'sleep' in query:
            speak('Okay sir, you can call me anytime.')
            break

if __name__ == "__main__":
    while True:
        permission = command()
        if "wake" in permission:
            greet()
            speak("You're being captured.")
            emotion = str(ed.emotion_retriver())
            recommendation(emotion)
        elif "mark" in permission:
            speak('Yes sir')
            assist()
        elif "goodbye" in permission:
            speak('Thankyou sir. Have a good day.')
            sys.exit()