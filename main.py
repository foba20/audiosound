import speech_recognition
import pyttsx3

import datetime

time = datetime.datetime.now()


def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def write_task():
    print("Что записать")

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open('task.txt', 'a') as file:
        file.write(query)
    print("Записал", query)


def hello():
    return "Привет, сэр"


with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()


if query == "привет":
    print('Привет, сэр')
elif 'время' in query:
    talk(time)
elif 'прочти' in query:
    with open('task.txt','r', encoding='utf-8') as file:
        talk(file.read())
else:
    print('Не понимаю')
