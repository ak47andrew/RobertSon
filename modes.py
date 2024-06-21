from helper import detect_command, remove_mention, say_text, translate as helper_translate, get_language
import functions


def normal(text: str, _) -> None:
    language = 'ru'
    text, detect = remove_mention(text)
    if not detect:
        print("No mention")
        return

    command_info = detect_command(text)
    if command_info is None:
        print("No command")
        return
    command, args = command_info

    print(f"Command named {command} found")
    output = getattr(functions, command)(*args)
    if output is None:
        print("No output")
        return
    say_text(output)


def translate(text: str, data: str) -> None:
    fl, tl = get_language(data)
    if text == 'роберт хватит':
        exit()
    
    elif 'роберт перейди в режим перевода' in text:
        translate()

    else:
           trans = helper_translate(text, fl, tl)
           say_text(trans, tl)
