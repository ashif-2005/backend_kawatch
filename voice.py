import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm currently unavailable.")
            return ""

# Function to process user's command
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I'm sorry, I don't understand.")

# Main program loop
while True:
    command = listen()
    process_command(command)

