from wake_word import listen_for_wake_word
from vad_listener import listen_vad
from intent_logic import handle_command
from tts import speak

def main():
    if listen_for_wake_word():
        while True:
            command = listen_vad()
            if command and ("exit" in command or "stop" in command):
                speak("Goodbye, shutting down.")
                break
            response = handle_command(command)
            speak(response)

if __name__ == "__main__":
    main
