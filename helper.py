from speech_recognition.recognizers import google
import speech_recognition as sr
from fuzzywuzzy import process
from gtts import gTTS
import os
from contextlib import suppress
from typing import Callable, Optional
from consts import names, commands

def record_sample(r) -> str:
    with sr.Microphone() as mic:
        audio = r.listen(mic)
    return google.recognize_legacy(r, audio, language="ru").lower()


def detect_mention(str) -> bool:
    # O(n)
    for name in names:
        if name in str:
            return True
    return False


def detect_command(str) -> Optional[Callable]:
    command = process.extractOne(str, commands.keys(), score_cutoff=80)
    if command is None:
        return
    return commands[command[0]]


def say_text(str, lang: str = 'ru'):
    filename = "output.mp3"
    with suppress(FileNotFoundError):
        os.remove(filename)
    res = gTTS(text=str, lang=lang)
    res.save(filename)

    if os.name == 'nt':  # Windows
        os.system('start ' + filename)
    else:  # Unix
        os.system('afplay ' + filename)

    

