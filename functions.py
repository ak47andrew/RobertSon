from helper import get_normal_form, translate
from consts import hello_aliases
from datetime import datetime


def echo(text: str):
    return text


def exit_app():
    exit()


def about_me(*_):
   return ("Меня зовут Роберт. Я универсальный робот-переводчик, владеющий пятьюдесятью языками и диалектами а также русским языком глухонемых. Я умею распознавать и воспроизводить язык жестов и обычную устную речь")


def help(*_):
    return ("Чтобы перейти в режим перевода скажите: Роберт, перейди в режим перевода с первого языка на второй. Например: с английского на испанский.Чтобы выйти из режима перевода скажите Роберт, перейди в нормальный режим")


def hi(name: str) -> str:
    form = get_normal_form(name)
    form = hello_aliases.get(form, form)
    return f"Привет, {form}"
