import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process user commands
def process_command(command):
    # Convert the command to lowercase for easier processing
    command = command.lower()

    if "hello" in command:
        speak("Hello! How can I assist you?")

    elif "open whatsapp" in command:
        url = "https://web.whatsapp.com/"
        speak("Opening website")
        webbrowser.open(url)

    elif "open chat gpt" in command:
        url = "https://chat.openai.com/"
        speak("Opening website")
        webbrowser.open(url)


  

    elif "current time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# Main program loop
while True:
    try:
        # Record audio from microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Convert speech to text
        command = recognizer.recognize_google(audio)

        # Print the recognized command
        print("Command:", command)

        # Process the command
        process_command(command)

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")

    except sr.RequestError:
        print("Sorry, I encountered an error. Please try again.")
