import speech_recognition as sr
import pyttsx3
import openai
import datetime
import pywhatkit
import os

from wake_word import listen_for_wake_word
from stt import SpeechToText
from intent_logic import handle_command
from tts import speak
from command_logic import recognize_command

stt_engine = SpeechToText(use_vad=True)

#to be fixed ; not recommeended to add API keys on GITHUB
os.environ["OPENAI_API_KEY"] = "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"
client = openai.OpenAI()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def main():
    # Start with wake word detection
    if listen_for_wake_word():
        while True:
            # Listen to user input
            command = stt_engine.listen()

            if command:
                # Check if user wants to exit
                if "exit" in command or "stop" in command:
                    speak("Goodbye, shutting down.")
                    break

                # Process command and generate response
                response = recognize_command(command)

                if not response:
                    response = handle_command(command)

                # Speak the response out loud
                if response:
                    speak(response)

if __name__ == "__main__":
    main()
