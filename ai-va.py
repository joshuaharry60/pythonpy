import pyttsx3
from google import genai
import speech_recognition as sr
import os
import dotenv
dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize pyttsx3 engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    print("AI", text)
    engine.runAndWait()
    
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening speak...")
        voice = r.listen(source)
    try:
        command = r.recognize_google(voice)
        print("you said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results if error for API; {e}")
        return ""
    