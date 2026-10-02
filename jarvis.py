from datetime import datetime
import json
print("Jarvis here.")


def User():
    while True:

        command = input(" Ask Anything: ")
        if command == "hello":
            print("HI")

        elif command == "name":
            print("Jarvis")

        elif command == "help":
            print("Available commands")
            print("hello")
            print("name")
            print("date")
            print("time")
            print("exit")

        elif command == "date":
            print(datetime.now().date())

        elif command == "time":
            print(datetime.now().strftime("%I:%M %p"))

        elif command == "note":
            with open("notes.txt", "a") as f:
                note = input("what should i remember?\n")
                f.write(note + "\n")

        elif command == "notes":
            with open("notes.txt", "r") as f:
                print(f.read())

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("I don't understand that command.")


User()
