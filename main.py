import subprocess
import sys

# Continuously start the voice recognition process, wait for it to finish, then start the command executor process
while True:
    voice_recognition = subprocess.Popen(["python3", "voice_recognition.py"], stdout=subprocess.PIPE)
    command, _ = voice_recognition.communicate()
    command = command.decode().strip()
    # print(command)
    if command:
        command_executor = subprocess.Popen(["python3", "command_executor.py", command])
        command_executor.wait()
