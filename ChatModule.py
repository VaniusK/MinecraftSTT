import keyboard
import time
import json
import pydirectinput
import pyperclip
eps = 0.001
layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                           'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                           "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))

config = json.load(open("config.json"))
language = config["Language"]

def paste(text):
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    pydirectinput.keyDown("ctrl")
    pydirectinput.keyDown("v")

    pydirectinput.keyUp("ctrl")
    pydirectinput.keyUp("v")
    pyperclip.copy(buffer)

def resetKeys():
    keys = [
        'ctrl'
    ]
    for key in keys:
        pydirectinput.keyUp(key)
        pydirectinput.keyDown(key)

def sendMessage(message):
    keyboard.press_and_release("t", eps)
    paste(message)
    keyboard.press_and_release("Enter", eps)
    resetKeys()


