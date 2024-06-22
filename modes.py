# импортирование необходимых данных из других файлов 
from helper import detect_command, remove_mention, say_text, translate as helper_translate, get_language, change_mode
import functions

# импортирование модуля для перевода
from deep_translator import GoogleTranslator


# нормальный режим
def normal(text: str, _) -> None:

    # в нормальном режиме робот принимает команды только на русском языке
    language = 'ru'

    # определение и удаление имени робота из принятого текста
    text, detect = remove_mention(text)

    # если имя не упоминалось,команда не будет принята и выведется текст об отсутствии упоминания
    if not detect:
        print("No mention")
        return
    

    # определение команды
    command_info = detect_command(text)

    # если не удалось определить никакую команду, информация об этом выводится
    if command_info is None:
        print("No command")
        return
    
    # команда и её параметры возвращаются функцией  detect_command
    command, args = command_info


    # вывод распознанной команды
    print(f"Command named {command} found")

    # определение того, что надо вывести или сказать
    # формируется из того, что возвращает функция, вызванная командой
    output = getattr(functions, command)(*args)
    if output is None:
        print("No output")
        return
    
    # синтез речи из аутпута
    say_text(output)


# режим превода
def translate(text: str, data: str) -> None:

    # получение языков перевода, которые возвращает функция get_language()
    fl, tl = get_language(data)

    #если на языке, с которого осуществляется перевод, сказать "стоп", программа завершит работу                                              
    if text == GoogleTranslator(source='ru', target =fl).translate('стоп'):
        exit()

    elif GoogleTranslator(source='ru', target=fl).translate('перейди в режим перевода') in text:
        change_mode(normal, translate, data)
    
    elif text == GoogleTranslator(source='ru', target=fl).translate('вернись в нормальный режим'):
        pass

    else:
           trans = helper_translate(text, fl, tl)
           say_text(trans, tl)

