import wave
import speech_recognition as sr
from vad_listener import AudioStream
import os
import datetime

class SpeechToText:
    # initializing the SpeechToText engine
    # :param use_vad: If True, use Voice Activity Dection (VAD) for input
    #   Else, use direct microphone input
    # :param confidence_threshold: inimum confidence (0-1) to accept recognized speech
   
    def __init__(self, use_vad=True, confidence_threshold=0.6):
        self.recognizer = sr.Recognizer()
        self.use_vad = use_vad
        self.confidence_threshold = confidence_threshold
    
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

        try:
            with sr.AudioFile(temp_filename) as source:
                audio = self.recognizer.record(source)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")

                # simulate confidence threshold with a whitelist override
                whitelist = ["exit", "stop", "goodbye"]

                if len(command.split()) >= 2 or command.lower() in whitelist:
                    self._log_command(command)
                    return command.lower()
                else:
                    print("Low confidence detected, please speak more clearly.")
                    return None


        except sr.UnknownValueError:
            print("Sorry, I didn't quite catch that.")
            return None
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return None
        finally:
            # Always delete temp file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    def _log_command(self, command):
        """
        Save recognized command into a log file with timestamp.
        """
        with open("commands.log", "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {command}\n")   
