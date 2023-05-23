from vosk import Model, KaldiRecognizer
import pyaudio
import json
import sys

# Vosk model path
model = Model(lang="ru")

# Set up audio input
p = pyaudio.PyAudio()
device_index = 0  # replace with the index of your ReSpeaker device
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000, input_device_index=device_index)

# Set up voice recognition
rec = KaldiRecognizer(model, 16000)

# Valid commands
valid_commands = ["алиса включи свет", "алиса выключи свет", "алиса скажи температуру", "алиса расскажи анекдот","алиса что делать"]

# Continuously listen for commands
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if 'text' in result:
            command = result['text']
            #print(command)
            # If the recognized command is valid, print it to stdout and exit the process
            if command in valid_commands:
                print(command)  
                sys.exit(0)
