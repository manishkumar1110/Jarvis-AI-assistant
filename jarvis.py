from datetime import datetime
import json
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
speak("Hello, I am Jarvis")


print("Jarvis here.")


def User():
    while True:

        with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

                try:
                    command = recognizer.recognize_google(audio).lower()
                    print("You:", command)

                except sr.UnknownValueError:
                    print("I didn't understand.")
                    continue

                except sr.RequestError:
                    print("Speech service unavailable.")
                    continue
        if command == "hello":
            speak("HI")

        elif command == "name":
            speak("Jarvis")

        elif command == "help":
            speak("Available commands")
            speak("hello")
            speak("name")
            speak("date")
            speak("time")
            speak("exit")

        elif command == "date":
            speak(datetime.now().date())

        elif command == "time":
            speak(datetime.now().strftime("%I:%M %p"))

        elif command == "note":
            with open("notes.txt", "a") as f:
                note = input("what should i remember?\n")
                f.write(note + "\n")

        elif command == "notes":
            with open("notes.txt", "r") as f:
                print(f.read())

        elif command == "exit":
            speak("Goodbye!")
            break

        else:
            speak("I don't understand that command.")


User()
