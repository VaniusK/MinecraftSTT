import ChatModule
import Google
import json
import keyboard
import Microphone
import time
import speech_recognition as sr
config = json.load(open("config.json"))
prefix = config["Prefix"]
startKey = config["StartKey"]
if startKey == "None":
    startKey = None
stopKey = config["StopKey"]
if stopKey == "None":
    stopKey = None
necessaryKey = config["NecessaryKey"]
if necessaryKey == "None":
    necessaryKey = None
extraRecordingTime = int(config["ExtraRecordingTime"])

r = sr.Recognizer()

while True:
    while not keyboard.is_pressed(startKey.lower()) and not keyboard.is_pressed(startKey.upper()):
        pass
    print("Recording audio")
    with sr.Microphone() as source:
        audio = r.recordUntilKeyPressed(source, stopKey=stopKey, necessaryKey=necessaryKey, extraRecordingTime=extraRecordingTime)
    text = Google.transcribeAudio(audio)
    text = text.lower()
    if len(text) > 0:
        if text[0].isalpha():
            text = text[0].upper() + text[1:]
        print(text)
        ChatModule.sendMessage(prefix + text)

