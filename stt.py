import wave
import speech_recognition as sr
from vad_listener import AudioStream

def listen():
    # Initialize VAD stream and get voice-only audio
    vad = AudioStream()
    audio_data = vad.listen_and_detect()

    # Save to temporary WAV file
    with wave.open("temp_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(audio_data)

    # Use SpeechRecognition to convert audio to text
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp_audio.wav") as source:
        audio = recognizer.record(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return None
