#импортирование необходимых библиотек и данных из других файлов
from speech_recognition.recognizers import google
import speech_recognition as sr
from gtts import gTTS
import os
from contextlib import suppress
from typing import Callable, Optional
from consts import names, commands, mode_regex, modes, from_language
from consts import to_language, from_language_default, to_language_default, languages
import pymorphy3
import re
from deep_translator import GoogleTranslator


# инструмент для анализа слова
morph = pymorphy3.MorphAnalyzer()


# запись речи, из которой будут определяться упоминания, команды и тп
def record_sample(r: sr.Recognizer, language) -> str:
    
    # для записи используется микрофон
    with sr.Microphone() as mic:
        audio = r.listen(mic)

    # функция переводит аудио в строку и возвращает его в виде текста
    return google.recognize_legacy(r, audio, language=str(language)).lower()


# удаление упоминания робота из текста
def remove_mention(text: str) -> tuple[str, bool]:
    
    # переменная flag показывает наличие или отсутствие упоминания
    # по дефлоту она принимает значение, равное логическому нулю
    flag = False

    # перебираются все возможные имена
    for name in names:

        # если имя встречается в тексте, оно заменяется пустой строкой
        # и переменная flag принимает значение, равное логической единице
        if name in text:
            text = text.replace(name, " ")
            flag = True

        # функция возвращает текст без упоминания и информацию о наличии или отсутствии упоминания
    return text, flag


# функция для определения комманды (регулярные выражения)
def detect_command(text: str) -> Optional[tuple[Callable, tuple[str]]]:

    # перебирается список регулярных выражений на совпадения принятого текста с элементом сиска
    for regex in commands:
        obj = re.findall(regex, text)

    # если команда возвращается - она возвращается и вызывает соответствующую функцию
        if obj:
            return commands[regex], tuple(obj)
        
    return None


# фунуция для синтеза речи
def say_text(text: str, lang: str = 'ru'):

    # текст, который будет произноситься, до этого записывается в память или выводится
    # после этого текст переводится в аудиоформат
    filename = "output.mp3"

    # если файл существует, он удаляется из памяти
    with suppress(FileNotFoundError):
        os.remove(filename)

    # при помощи библиотеки gTTS текст преобразуется в речь
    res = gTTS(text=text, lang=lang)

    # результат сохраняется в аудиоформате
    res.save(filename)


    # файл проигрывается в системе (команда автоматически вводится в терминал компьютера)

    # для плеера windows
    if os.name == 'nt':  # Windows
        os.system('start ' + filename)

    # для плеера mac
    else:  # Unix
        os.system('afplay ' + filename)


# функция для перевода
def translate(text: str, from_lang: str, to_lang: str) -> str:

    # возвращает исходный текст, переведенный на запрошенный язык
    return GoogleTranslator(source=from_lang, target=to_lang).translate(text)
    
   
# функция для возвращения слова в начальную форму
# преобразование слов осуществляется при помощи модуля зньўкзр3
def get_normal_form(text: str) -> str:

    # возврвщает исходное слово в начальную форму
    return morph.parse(text)[0].normal_form


# функция для смены режима 
def change_mode(current_mode: str, text: str) -> tuple[str, str]:

    if len(k := re.findall(mode_regex, text)) == 0:
        return current_mode, ""
    
    a, b = k[0]
    c = a + b 
    c, *args = c.split()
    c = get_normal_form(c)
    args = " ".join(args)

    current_mode = modes.get(c, current_mode)

    # функция возвращает режим и его параметры
    return current_mode, args


# функция для определения языков, с которого и на который будет осуществляться перевод
def get_language(text: str) -> tuple[str, str]:
    k = re.findall(from_language, text)
    from_text = from_language_default if len(k) == 0 else k[0]
    from_text = get_normal_form(from_text)
    from_text = languages.get(from_text, from_language_default)

    k = re.findall(to_language, text)
    to_text = to_language_default if len(k) == 0 else k[0]
    to_text = get_normal_form(to_text)
    to_text = languages.get(to_text, to_language_default)

    return from_text, to_text

