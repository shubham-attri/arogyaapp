# import speech_recognition as sr
# import pyttsx3
#
# # Initialize the speech recognizer and the speech engine
# r = sr.Recognizer()
# engine = pyttsx3.init()
#
# # Define a function to listen for and recognize speech
# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print("You said:", text)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, I didn't catch that.")
#         return None
#
# # Define a function to speak a response
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
# # Main loop for the AI bot
# while True:
#     text = recognize_speech()
#     if text is not None:
#         if "hello" in text.lower():
#             speak("Hello! How can I help you today?")
#         elif "what can you do" in text.lower():
#             speak("I can provide information about the features of this app, and I can help you navigate to different features. Just ask me!")
#         elif "open events and activities" in text.lower():
#             speak("Opening events and activities...")
#             # Code to navigate to the events and activities feature
#         elif "open my schedule" in text.lower():
#             speak("Opening my schedule...")
#             # Code to navigate to the my schedule feature
#
#         elif"exit" in text.lower() or "quit" in text.lower() or "goodbye" in text.lower():
#             speak("Goodbye!")
#             break
#         else:
#             speak("I'm sorry, I didn't understand that.")

# In the ai_bot.py file, import the necessary Python packages:
import speech_recognition as sr
import pyttsx3
import os


# Define a function to listen for and recognize speech
def respond_to_command(command):
    if "hello" in command:
        return "Hi there!"
    elif "what is this app" in command:
        return "This is a personal assistant app that helps you with daily tasks such as finding helpers, tracking routines, and setting reminders."
    elif "open home services" in command:
        os.system("start http://localhost:3000/home-services")
        return "Opening home services page"
    else:
        return "Sorry, I didn't understand your command"

# Initialize the speech recognition and text-to-speech engines:
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Create a function to listen for the user's voice command:
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I didn't understand your command"

# Create a function to speak the AI bot's response:
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Create a main loop for the AI bot:
while True:
    command = listen_for_command()
    response = respond_to_command(command)
    speak(response)

    if "exit" in command or "quit" in command or "goodbye" in command:
        speak("Goodbye!")
        break
