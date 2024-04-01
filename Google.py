import speech_recognition as sr
import json

r = sr.Recognizer()
config = json.load(open("config.json"))
language = config["Language"]



def transcribeAudio(audio):
    print("Sending request to Google")
    try:
        text = r.recognize_google(audio, language=language)
    except:
        text = ""
    return text


