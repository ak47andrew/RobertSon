from speech_recognition.recognizers import google
import speech_recognition as sr
from gtts import gTTS
import os
from contextlib import suppress
from typing import Callable, Optional
from consts import names, commands, mode_regex, modes, from_language, to_language, from_language_default, to_language_default, languages
import argostranslate.translate
import pymorphy3
import re


morph = pymorphy3.MorphAnalyzer()


def record_sample(r: sr.Recognizer) -> str:
    """
    Records audio input from the user's microphone and uses the Google Speech Recognition library to convert it to text.

    Args:
    r (sr.Recognizer): An instance of the `SpeechRecognizer` class from the `speech_recognition` library.

    Returns:
    str: The transcribed text from the user's audio input, converted to lowercase.

    The function uses the `sr.Microphone` context manager to obtain audio input from the user's microphone. 
    It then listens to the audio input using the `r.listen(mic)` method, where `mic` is the `sr.Microphone` 
    instance obtained from the context manager. Finally, it uses the `google.recognize_legacy` function 
    to transcribe the audio into text, and returns the transcribed text as a lowercase string.
    """
    with sr.Microphone() as mic:
        audio = r.listen(mic)
    return google.recognize_legacy(r, audio, language="ru").lower()


def remove_mention(text: str) -> tuple[str, bool]:
    """
    Removes specified names from the input text and returns the modified text along with a boolean flag indicating whether any names were removed.

    Args:
    text (str): The input text to be modified.

    Returns:
    tuple[str, bool]: A tuple containing the modified text and a boolean flag indicating whether any names were removed.

    The function iterates through the list of names and replaces any occurrences of a name in the input text 
    with an empty string. If any names are found and replaced, the function returns the modified text 
    along with a boolean flag set to `True`. If no names are found in the input text, 
    the function returns the original text along with a boolean flag set to `False`.
    """
    flag = False
    for name in names:
        if name in text:
            text = text.replace(name, " ")
            flag = True
    return text, flag


def detect_command(text: str) -> Optional[tuple[Callable, tuple[str]]]:
    """
    Detects commands in the input text and returns a tuple containing the corresponding function and its arguments, if any.

    Args:
    text (str): The input text to be analyzed for commands.

    Returns:
    Optional[tuple[Callable, tuple[str]]]: A tuple containing the corresponding function and its arguments, if any, or `None` if no commands are found.

    The function iterates through the list of command regular expressions and checks if any of them 
    match the input text. If a match is found, the function returns a tuple containing the corresponding function 
    and its arguments, extracted from the input text. If no commands are found in the input text, the function returns `None`.
    """
    for regex in commands:
        obj = re.findall(regex, text)
        if obj:
            return commands[regex], tuple(obj)

    return None


def say_text(text: str, lang: str = 'ru'):
    """
    Converts the input text to speech and saves it as an audio file.

    Args:
    text (str): The input text to be converted to speech.
    lang (str): The language of the input text. Defaults to 'ru'.

    Returns:
    None: The function does not return any value, as it saves the generated audio file.

    The function uses the `gTTS` library to convert the input text to speech. The generated audio file is saved 
    with the filename "output.mp3". If the file already exists, it is first removed before the new audio file is saved. 
    The function also checks the operating system and uses the appropriate command to start the audio playback.
    """
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
    """
    Translates the input text from the specified source language to the specified target language.

    Args:
    text (str): The input text to be translated.
    from_lang (str): The source language of the input text.
    to_lang (str): The target language to which the input text should be translated.

    Returns:
    str: The translated text in the specified target language.

    The function uses the `argostranslate.translate` library to translate the input text from the specified source 
    language to the specified target language. The translated text is then returned as a string.
    """
    return argostranslate.translate.translate(text, from_lang, to_lang)

def get_normal_form(text: str) -> str:
    """
    Returns the normal form of the input text.

    Args:
    text (str): The input text to be processed.

    Returns
    str: The normal form of the input text.

    The function uses the `pymorphy3` library to parse the input text and returns the normal form of the first word 
    in the text. The normal form is the base form of a word, which is the form that is used as the dictionary entry for the word.
    """
    return morph.parse(text)[0].normal_form


def change_mode(current_mode: str, text: str) -> tuple[str, str]:
    """
    Changes the current mode based on the input text and returns the new current mode along with any additional arguments.

    Args:
    current_mode (str): The current mode of the application.
    text (str): The input text to be analyzed for mode changes.

    Returns
    tuple[str, str]: A tuple containing the new current mode and any additional arguments extracted from the input text. 
    If no mode changes are detected, the function returns the original current mode 
    and an empty string as the additional argument.

    The function first checks if the input text contains a mode change pattern. If a match is found, 
    the function extracts the corresponding mode and any additional arguments from the input text. 
    The function then updates the current mode based on the extracted mode and returns the new current mode 
    along with any additional arguments. If no mode changes are detected, the function returns the original current mode 
    and an empty string as the additional argument.
    """
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
    """
    Returns the source language and target language extracted from the input text.

    Args
    text (str): The input text to be analyzed for languages.

    Returns
    tuple[str, str]: A tuple containing the source language and target language extracted from the input text. 
    If no languages are detected, the function returns the default source and target languages.

    The function first checks if the input text contains the source language pattern. If a match is found, 
    the function extracts the corresponding source language from the input text. Similarly, the function checks 
    for the target language pattern and extracts the corresponding target language. The function then returns 
    the extracted source and target languages as a tuple. If no languages are detected, the function returns 
    the default source and target languages.
    """
    k = re.findall(from_language, text)
    from_text = from_language_default if len(k) == 0 else k[0]
    from_text = get_normal_form(from_text)
    from_text = languages.get(from_text, from_language_default)

    k = re.findall(to_language, text)
    to_text = to_language_default if len(k) == 0 else k[0]
    to_text = get_normal_form(to_text)
    to_text = languages.get(to_text, to_language_default)

    return from_text, to_text