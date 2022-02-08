'''
#Reconhecimento de voz pelo google
import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#Abre o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #Define o microfone como fonte de áudio

        print(r.recognize_google(audio, language='pt'))
'''

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

#Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)

engine.say("Eu vou falar esse Texto")
engine.RunAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.pyInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

#Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveForm(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)

            if text == 'que horas são' or text == 'me diga o horario':
                speak(core.SystemInfo.get_time())