import speech_recognition as sr
import pyttsx3
import openai
import datetime
import pywhatkit
import os

os.environ["OPENAI_API_KEY"] = "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"
client = openai.OpenAI()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Waiting for 'Hey Aztec'...")
        while True:
            audio = recognizer.listen(source)
            try:
                phrase = recognizer.recognize_google(audio).lower()
                if "hey aztec" in phrase:
                    print("Wake word detected!")
                    return
            except:
                pass

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Service is currently unavailable.")
            return None

def get_ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    listen_for_wake_word()
    while True:
        command = listen()
        if command:
            if "stop" in command or "exit" in command:
                speak("Goodbye, Aztec out.")
                break
            response = get_ai_response(command)
            print("Assistant:", response)
            speak(response)

if __name__ == "__main__":
    main()
