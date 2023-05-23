# import paho.mqtt.client as mqtt
# import pyttsx3
# import time
# import sys

# command = sys.argv[1]  # The command is passed as a command-line argument

# # Initialize the Speech Engine
# engine = pyttsx3.init()

# # Set properties _before_ you add things to say
# engine.setProperty('rate', 150)    # Speed percent (can go over 100)
# engine.setProperty('volume', 0.8)  # Volume 0-1

# # Change voice to Russian (may depend on your system configuration)
# voices = engine.getProperty('voices')
# for voice in voices:
#     if "russian" in voice.languages:
#         engine.setProperty('voice', voice.id)
#         break

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # MQTT settings
# MQTT_USER = "atc-festu"
# MQTT_PASSWORD = "00000"
# MQTT_ADDRESS = "raspberrypi.local"

# # Create the MQTT client
# client = mqtt.Client()

# # Set MQTT credentials
# client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# # Connect to the MQTT broker
# client.connect(MQTT_ADDRESS, 1883)
# client.loop_start()

# # Listen for specific commands
# if command == "олег включи свет":
#     client.publish("esp32/relay", "on")
#     speak("Свет включен")
# elif command == "олег выключи свет":
#     client.publish("esp32/relay", "off")
#     speak("Свет выключен")
# elif command == "олег скажи температуру":
#     speak("Температура 25 градусов по цельсию")
import paho.mqtt.client as mqtt
import os
import sys

command = sys.argv[1]  # The command is passed as a command-line argument

# def speak(text):
#     # os.system(f'espeak-ng -v ru "{text}"')
#     os.system(f'espeak-ng -v ru+f4 -p 99 -s 90 "{text}"')

# def speak_man(text):
#     # os.system(f'espeak-ng -v ru "{text}"')
#     os.system(f'espeak-ng -v ru+4 "{text}"')

# def speak_fbi(text):
#     # os.system(f'espeak-ng -v ru "{text}"')
#     os.system(f'espeak-ng -v ru+2 "{text}"')


def speak(text):
    os.system(f'echo "{text}" | spd-say  --wait -o rhvoice -l ru  -e -t female1')

def speak_man(text):
    os.system(f'echo "{text}" | spd-say  --wait -o rhvoice -l ru  -e -t male1')

def speak_fbi(text):
    os.system(f'echo "{text}" | spd-say  --wait -o rhvoice -l ru  -e -t female1')

# MQTT settings
MQTT_USER = "atc-festu"
MQTT_PASSWORD = "00000"
MQTT_ADDRESS = "raspberrypi.local"

# Create the MQTT client
client = mqtt.Client()

# Set MQTT credentials
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Connect to the MQTT broker
client.connect(MQTT_ADDRESS, 1883)
client.loop_start()

# Listen for specific commands
if command == "алиса включи свет":
    client.publish("esp32/relay", "on")
    speak("Свет включен")
elif command == "алиса выключи свет":
    client.publish("esp32/relay", "off")
    speak("Свет выключен")
elif command == "алиса скажи температуру":
    speak("Температура 25 градусов по цельсию")
elif command == "алиса расскажи анекдот":
    speak_man("Мама пишет сыну в тюрьму: Сынок как тебя посадили сил нет")
    speak_man("некому помогать по хозяйству")
    speak_man("Огород не вскопанный, картошка не посажена, что делать не знаю")
    speak_man("Сын пишет ответ Мама в огороде не копайся, накопаешь такого, что и тебя посадят, и мне срок добавят!")
    speak_man("Мама опять пишет сыну: Сынок как пришло твоё письмо, приехали мусора перекопали весь огород,")
    speak_man("ничего не нашли и уехали злые.")
    speak_man("Сын пишет: Мама, чем мог тем помог. Картошку сажайте сами!")
elif command == "алиса что делать":
    speak_fbi("отец знакомого работает в ФСБ. Сегодня срочно вызвали на совещание.")
    speak_fbi("Вернулся поздно и ничего не объяснил. Сказал лишь собирать вещи")
    speak_fbi("и бежать в магазин за продуктами на две недели. Сейчас едем куда-то далеко за город.")
    speak_fbi("Не знаю что происходит, но мне кажется началось...")