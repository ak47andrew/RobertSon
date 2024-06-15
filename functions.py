from consts import names, commands


def clean_up_text(text):
    for i in names + tuple(commands.keys()):
        text = text.replace(i, "")
    return text


def echo(str):
    return clean_up_text(str)


def exit_app(*_):
    exit()


# def translate(str):
#     translated = argostranslate.translate.translate(clean_up_text(str), "ru", "ja")
#     say_text(translated, "ja")


def hi_dad(*_):
    return "Привет, папа Квас"


def hi_mom(*_):
    return "Привет, мама Аля"


def hi_vlad(*_):
    return "Привет, Влад"
