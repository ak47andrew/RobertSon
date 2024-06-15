import argostranslate.package
import argostranslate.translate
from consts import names, commands
from helper import say_text
import speech_recognition as sr


def clean_up_text(text):
    for i in names + tuple(commands.keys()):
        text = text.replace(i, "")
    return text


def echo(str):
    return clean_up_text(str)


def exit_app(*_):
    exit()


def translate(str):
    translated = argostranslate.translate.translate(clean_up_text(str), "ru", "ja")
    say_text(translated, "ja")


def hi_dad(*_):
    say_text("Привет, папа Квас")


def hi_mom(*_):
    say_text("Привет, мама Аля")


def hi_vlad(*_):
    say_text("Привет, Влад")


def durable_translation(*_):
    while True:
        print("Recording...")
        try:
            text = record_sample(r)
        except sr.UnknownValueError:
            print("No audio provided")
            continue

        print(text)
        translated = argostranslate.translate.translate(clean_up_text(text), "ru", "ja")
        say_text(translated, "ja")

    
    
     
        
    

