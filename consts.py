﻿# импортирование регулярных выражений
import re

# импортирование модуля для перевода
from deep_translator import GoogleTranslator


# схема переключения режимов по регулярным выражениям
mode_regex = re.compile(r"перейди в (.*)режим(.*)")


# имена, на которые отзывается робот
names = [
    "роберт",
    "роберта",
    "роба",
    "робка",
    "робко",
    "коробка",
]


# комманды, которые может выполнять робот (регулярные выражения)
# первая колонка - команды, вторая - функции, которые им соответствуют
commands = {
    r"(?:скажи|повтори) (.*)": "echo",
    r"поздоровайся с ([\w ]+)": "hi",
    r"стоп|хватит|выход|достаточно": "exit_app",
    r"кто ты|кто ты такой": "about_me",
    r"ты говоришь на": "check language",
    r"как включить режим перевода|как перейти в режим перевода": "help",
    r"как выйти из режима перевода|как перейти в нормальный режим": "help",
}


# названия режимов
modes = {
    "нормальный": "normal",
    "классический": "normal",
    "стандартный": "normal",
    "перевод": "translate",
}


# имена, с которыми надо здороваться как-то по-особенному
# первая колонка - имя, втоорая - что нужно произносить при приветствии
hello_aliases = {
    "папа": "папа Квас",
    "мама": "мама Аля",
    "влад": "о великий предводитель проводов и тридэ принтеров",
    "юлия николаевна": "Юлия николаевна",
    "сергеем сергеевич": "самый лучший мужчина в мире",
    "товарищем сталин": "тимофей",
}


# список поддерживаемых языков 
#первая колонка - язык, вторая - его код по ISO 639-1
languages = {
    'африкаанс|африканский': 'af', 
    'албанский':'sq',
    'арабский': 'ar', 
    'бенгальский': 'bn', 
    'боснийский': 'bs', 
    'болгарский': 'bg', 
    'каталонский': 'ca', 
    'китайский (simplified)': 'zh-CN',
    'китайский (traditional)': 'zh-TW', 
    'чешский': 'cs', 
    'датский': 'da', 
    'немецкий': 'de', 
    'греческий': 'el', 
    'голландский|нидерландский':'nl',
    'иврит': 'iw', 
    'хинди': 'hi', 
    'венгерский': 'hu', 
    'исландский': 'is', 
    'индонезийский': 'id', 
    'итальянский': 'it', 
    'японский': 'ja', 
    'яванский': 'jw', 
    'каннада': 'kn',  
    'кхмерский': 'km', 
    'корейский': 'ko', 
    'латынь|латинский': 'la', 
    'латышский': 'lv', 
    'малайский': 'ms', 
    'малаялам': 'ml', 
    'маратхи': 'mr', 
    'мьянманский': 'my', 
    'непальский': 'ne', 
    'норвежский': 'no', 
    'польский': 'pl', 
    'португальский': 'pt', 
    'румынский': 'ro', 
    'русский': 'ru', 
    'сербский': 'sr', 
    'сингальский': 'si', 
    'словакский': 'sk', 
    'испанский': 'es', 
    'суданский': 'su', 
    'суахили': 'sw', 
    'шведский': 'sv', 
    'тамильский': 'ta', 
    'телугу': 'te', 
    'тайский': 'th', 
    'турецкий': 'tr', 
    'украинский': 'uk', 
    'урду': 'ur', 
    'вьетнамский': 'vi', 
}


# регулярные выражения для определения языков ввода и вывода текста
# (с какого и на какой язык будет осуществляться перевод)
from_language = re.compile(r"с (\w+)", re.UNICODE)
to_language = re.compile(r"на (\w+)", re.UNICODE)


# определение языков перевода, если они не были названы

# если язык, с которого будет осуществляться перевод, не был назван, перевод
# будет автоматически осуществляться с русского языка
from_language_default = "ru"

# если язык, на который будет осуществляться перевод, не был назван, перевод
# будет автоматически осуществляться на английский язык
to_language_default = "en"

