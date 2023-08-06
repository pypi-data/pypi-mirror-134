from pynput import keyboard
import json
import os

on_record = False
number = ""

def print_char(num):
    controller = keyboard.Controller()
    if num in data:
        for i in range(len(number) + 2):
            controller.press(keyboard.Key.backspace)
            controller.release(keyboard.Key.backspace)
        controller.type(data.get(num))

def on_press(key):
    global on_record
    global number
    key = str(key).replace("'", "")

    if key == "[":
        on_record = True
    elif key == "]":
        on_record = False
        print_char(number)
        number = ""
    elif key == str(keyboard.Key.backspace).replace("'", "") and on_record == True:
        if number == "":
            on_record = False
        else:
            number = number[:-1]
    elif on_record == True:
        number += key

data = None

def main():
    os.chdir(os.path.dirname(__file__))
    global data
    with open("char.json", "r", encoding = "utf8") as f:
        data = json.loads(f.read())

    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
