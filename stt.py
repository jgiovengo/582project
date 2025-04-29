import wave
import speech_recognition as sr
from vad_listener import AudioStream

class SpeechToText:
    # initializing the SpeechToText engine
    # param: use_vad: If True, use Voice Activity Dection 
    # (VAD) for input
    # Else, use direct microphone input
    def __init__(self, use_vad=True):
        self.recognizer = sr.Recognizer()
        self.use_vad = use_vad
    
    #main method to listen & return recognized speech
    def listen(self):
        if self.use_vad:
            return self._listen_with_vad()
        else:
            return self._listen_microphone()
        
    #listen from microphone    
    def _listen_microphone(self):
        with sr.Microphone() as source:
            print("Listening (microphone)...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't quiet catch that.")
                return None
            except sr.RequestError():
                print("Speech recognition service unavailable.")
                return None
            
    # use VAD to capture and recognize speech
    def _listen_with_vad(self):
        vad = AudioStream()
        audio_data = vad.listen_and_detect()

        temp_filename = "temp_audio.wav"
        with wave.open(temp_filename, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(audio_data)

        with sr.AudioFile(temp_filename) as source:
            audio = self.recognizer.record(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
            except sr.UnknownValueError:
                print("Sorry, I didn't quiet catch that.")
                return None
            except sr.RequestError():
                print("Speech recognition service unavailable.")
                return None    

        














# def listen():
#     # Initialize VAD stream and get voice-only audio
#     vad = AudioStream()
#     audio_data = vad.listen_and_detect()

#     # Save to temporary WAV file
#     with wave.open("temp_audio.wav", "wb") as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)
#         wf.setframerate(16000)
#         wf.writeframes(audio_data)

#     # Use SpeechRecognition to convert audio to text
#     recognizer = sr.Recognizer()
#     with sr.AudioFile("temp_audio.wav") as source:
#         audio = recognizer.record(source)

#         try:
#             command = recognizer.recognize_google(audio)
#             print(f"You said: {command}")
#             return command.lower()
#         except sr.UnknownValueError:
#             print("Sorry, I didn't catch that.")
#             return None
#         except sr.RequestError:
#             print("Speech recognition service unavailable.")
#             return None
