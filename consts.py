import re


# Constants for names, commands, modes, hello_aliases, and languages
mode_regex = re.compile(r"перейди в (.*)режим(.*)")

# Names: List of names in Cyrillic script
names = [
    "роберт",
    "роберта",
    "роба",
    "робка",
    "робко",
    "коробка",
    "роберт квасович",
    "роберт андреевич",
]

# Commands: Dictionary of command patterns and their corresponding functions
commands = {
    r"(?:скажи|повтори) (.*)": "echo",
    r"поздоровайся с ([\w ]+)": "hi",
    r"стоп|хватит|выход|достаточно": "exit_app",
    r"кто ты|кто ты такой": "about_me",
    r"какими языками ты владеешь|какие языки ты знаешь": "languages_list",
    r"как включить режим перевода|как перейти в режим перевода|как выйти из режима перевода|как перейти в нормальный режим":"help",
}

# Modes: Dictionary of mode names and their corresponding values
modes = {
    "нормальный": "normal",
    "классический": "normal",
    "стандартный": "normal",
    "перевод": "translate",
}

# Hello aliases: Dictionary of aliases and their corresponding full names
hello_aliases = {
    "папа": "папа Квас",
    "мама": "мама Аля",
    "влад": "Влад",
    "юлия николаевна": "Юлия николаевна",
    "сергеем сергеевич": "самый лучший мужчина в мире",
    "товарищем сталин": "тимофей",
}

# Languages: Dictionary of language codes and their corresponding names
languages = {
    "русский": "ru",
    "английский": "en",
    "немецкий": "de",
    "французский": "fr",
    "итальянский": "it",
    "португальский": "pt",
    "шведский": "sv",
    "норвежский": "no",
    "испанский": "es",
    "финский": "fi",
    "турецкий": "tr",
    "чешский": "cs",
    "украинский": "uk",
    "польский": "pl",
    "нидерландский": "nl",
    "голландский": "nl",
    "испанский": "es",
    "японский": "ja",
}

# Regex patterns for language detection
from_language = re.compile(r"с (\w+)", re.UNICODE)
to_language = re.compile(r"на (\w+)", re.UNICODE)
from_language_default = "ru"
to_language_default = "en"
