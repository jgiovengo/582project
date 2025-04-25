import collections
import webrtcvad
import sys
import wave
import pyaudio
import os
import time

class AudioStream:
    def __init__(self, aggressiveness=2):
        self.vad = webrtcvad.Vad(aggressiveness)
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.frame_duration = 30  # ms
        self.chunk = int(self.rate * self.frame_duration / 1000)
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def start_stream(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()

    def listen_and_detect(self, timeout=10):
        self.start_stream()
        print("Listening for voice...")

        ring_buffer = collections.deque(maxlen=10)
        voiced_frames = []
        triggered = False
        start_time = time.time()

        try:
            while True:
                frame = self.stream.read(self.chunk, exception_on_overflow=False)
                is_speech = self.vad.is_speech(frame, self.rate)

                if not triggered:
                    ring_buffer.append((frame, is_speech))
                    num_voiced = len([f for f, speech in ring_buffer if speech])
                    if num_voiced > 0.8 * ring_buffer.maxlen:
                        triggered = True
                        voiced_frames.extend([f for f, s in ring_buffer])
                        ring_buffer.clear()
                else:
                    voiced_frames.append(frame)
                    ring_buffer.append((frame, is_speech))
                    num_unvoiced = len([f for f, speech in ring_buffer if not speech])
                    if num_unvoiced > 0.9 * ring_buffer.maxlen:
                        break

                if time.time() - start_time > timeout:
                    print("Timeout reached, no speech detected.")
                    break

            print("Voice detected, returning audio frames.")
            return b''.join(voiced_frames)
        finally:
            self.stop_stream()
