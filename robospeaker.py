import pyttsx3

if __name__ == "__main__":
    print("Welcome to robospeaker 1.1 created by Arfa")
    x = input("Enter what you want me to speak: ")
    data  = pyttsx3.init()
    data.say(x)
    data.runAndWait()