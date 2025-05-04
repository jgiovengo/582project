import speech_recognition as sr

def listen_for_wake_word(wake_word="hey aztec"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Waiting for wake word...")
        while True:
            try:
                audio = recognizer.listen(source)
                phrase = recognizer.recognize_google(audio).lower()
                if wake_word in phrase:
                    print("Wake word detected!")
                    return True
            except:
                continue
