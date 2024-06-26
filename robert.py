# импортирование необходимых библиотек и данных из других файлов
import modes
import speech_recognition as sr
from helper import record_sample, change_mode, get_language

#для распознавания речи используется функция из модуля speech_recognition
r = sr.Recognizer()
from gestures import *
# по умолчанию робот нвходится в нормальном режиме
# режим имеет пустые параметры
mode = "normal"
mode_args = ""


# основная функция программы, в которой происходит взаимодействие с пользователем
def main():
    
    # инициирование переменных 
    global mode, mode_args

    # приветствие, которое свидетельствует о том, что программа запустилась
    print("Добро пожаловать. Всё настроено и готово")

    # бесконечный цикл, который будет работать до тех пор, пока программа не будет закрыта
    while True:

        # если робот в нормальном режиме, язык, на котором он записывает речь - русский
        # в режиме перевода текст принимается на языке, с которого осуществляется перевод
        if mode == "normal":
            language = 'ru'
        elif mode == "translate":

            # языки перевода возвращает функция get_language
            fl, tl = get_language(text)
            language  = fl

        # ывводится для обозначения того, что робот уже слушает и записывает речь
        print("Recording...")

        # текст возвращается функцией record_sample
        # если текст не был получен, выводится информация об этом и речь продолжает записываться
        try:
            text = record_sample(r, language)
        except sr.UnknownValueError:
            print("No audio provided")
            continue

        # записанный текст выводится
        print(text)

        # режим меняется со старого на тот, который был указан 
        # в тексте, который только что был получен
        old_mode = mode
        mode = change_mode(mode, text)

        # определяется, какой из режимов был включён
        # установленному режиму передаются необходимые параметры
        if mode[0] == old_mode:

            mode = mode[0]
            getattr(modes, mode)(text, mode_args)
        else:
            mode_args = mode[1]
            mode = mode[0]
            
            # выводится информация о том, какой режим был включён
            print(f"Mode has been set to {mode}")


# если программа была вызвана из основого модуля, запускается главный цикл функции
if __name__ == '__main__':
    main()
