from flask import Flask, request
import speech_recognition as sr
import os
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            if "open google" in text.lower():
                webbrowser.open("https://www.google.com")
                return "Opened Google!"
            elif "what can this app do" in text.lower():
                return "This app can execute some commands based on your voice input."
            else:
                return "Sorry, I didn't understand what you said."
        except sr.UnknownValueError:
            return "Sorry, I could not understand what you said."
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)
    return "Hello, welcome to the audio input app!"

if __name__ == '__main__':
    app.run()
