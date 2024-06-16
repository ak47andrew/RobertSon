import re


# Constants for names, commands, modes, hello_aliases, and languages

# Names: List of names in Cyrillic script
names = [
    "роберт",
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
}

# Modes: Dictionary of mode names and their corresponding values
modes = {
    "нормальный": "noraml",
    "классический": "noraml",
    "стандартный": "noraml",
    "перевод": "translate",
}

# Hello aliases: Dictionary of aliases and their corresponding full names
hello_aliases = {
    "папа": "папа Квас",
    "мама": "мама Аля",
    "влад": "Влад",
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
