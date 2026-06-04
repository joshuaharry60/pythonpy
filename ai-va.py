import pyttsx3
from google import genai
import speech_recognition as sr
import pyaudio
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
    
speak("Hello, I am your AI assistant. How can I help you today?")
    