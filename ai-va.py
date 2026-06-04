import pyttsx3
from google import genai
import speech_recognition as sr
import pyaudio
import os
import dotenv
dotenv.load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Initialize pyttsx3 engine
engine = pyttsx3.init()


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except Exception as e:
        print(e)
        return None

# speak("hello am ready to assist you")
def get_ai_response(user_speech):
    prompt = f"make sure the answer is short and concise, answer the following question: {user_speech}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


while True:
    print("waiting for speech...")
    user_speech = listen()

    if user_speech:
        print("processing...")

        if "stop" in user_speech.lower():
            speak("Goodbye!")
            break

        ai_response = get_ai_response(user_speech)
        speak(ai_response)