from speech_recognition.recognizers import google
import speech_recognition as sr
from gtts import gTTS
import os
from contextlib import suppress
from typing import Callable, Optional
from consts import names, commands, mode_regex, modes, from_language, to_language, from_language_default, to_language_default, languages
import pymorphy3
import re
from deep_translator import GoogleTranslator


morph = pymorphy3.MorphAnalyzer()


def remove_mention(text: str) -> tuple[str, bool]:
    flag = False
    for name in names:
        if name in text:
            text = text.replace(name, " ")
            flag = True
    return text, flag


def detect_command(text: str) -> Optional[tuple[Callable, tuple[str]]]:
    for regex in commands:
        obj = re.findall(regex, text)
        if obj:
            return commands[regex], tuple(obj)

    return None


def say_text(text: str, lang: str = 'ru'):
    filename = "output.mp3"
    with suppress(FileNotFoundError):
        os.remove(filename)
    res = gTTS(text=text, lang=lang)
    res.save(filename)

    if os.name == 'nt':  # Windows
        os.system('start ' + filename)
    else:  # Unix
        os.system('afplay ' + filename)

def translate(text: str, from_lang: str, to_lang: str) -> str:
    return GoogleTranslator(source=from_lang, target=to_lang).translate(text)
    # return argostranslate.translate.translate(text, from_lang, to_lang)
   

def get_normal_form(text: str) -> str:
    return morph.parse(text)[0].normal_form


def change_mode(current_mode: str, text: str) -> tuple[str, str]:
    if len(k := re.findall(mode_regex, text)) == 0:
        return current_mode, ""

    a, b = k[0]  # Убейте меня за этот код ;(
    c = a + b  # Один из них по любому будет пустой строкой
    c, *args = c.split()
    c = get_normal_form(c)
    args = " ".join(args)

    current_mode = modes.get(c, current_mode)

    return current_mode, args


def get_language(text: str) -> tuple[str, str]:
    k = re.findall(from_language, text)
    from_text = from_language_default if len(k) == 0 else k[0]
    from_text = get_normal_form(from_text)
    from_text = languages.get(from_text, from_language_default)

    k = re.findall(to_language, text)
    to_text = to_language_default if len(k) == 0 else k[0]
    to_text = get_normal_form(to_text)
    to_text = languages.get(to_text, to_language_default)

    return from_text, to_text, from_language