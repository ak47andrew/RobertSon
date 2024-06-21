import modes
import speech_recognition as sr
import helper
from gtts import gTTS
from deep_translator import GoogleTranslator
from speech_recognition import google
import functions

r = sr.Recognizer()
mode = "normal"
mode_args = ""


def translate(text: str, data: str) -> None:
    fl, tl = get_language(data)
    if text == 'роберт хватит':
        exit()
    
   # elif 'роберт перейди в режим перевода' in text:
      #  command == 'перейди в режим перевода'

    else:
           trans = helper_translate(text, fl, tl)
           say_text(trans, tl)
    return fl
 

def record_sample(r: sr.Recognizer) -> str:
    with sr.Microphone() as mic:
        audio = r.listen(mic)
    lang:str
    
    if mode == 'normal':
        lang = 'ru'
    else:
        lang = functions.from_language
        

    return google.recognize_legacy(r, audio, language='ru').lower()

def normal(text: str, _) -> None:
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

def main():
    global mode, mode_args
    print("Добро пожаловать. Всё настроено и готово")

    while True:
        print("Recording...")
        try:
            text = record_sample(r)
        except sr.UnknownValueError:
            print("No audio provided")
            continue

        print(text)

        
        old_mode = mode
        mode = helper.change_mode(mode, text)


        if mode[0] == old_mode:
            mode = mode[0]
            # Call the corresponding mode function with the recognized text and mode arguments
            getattr(mode)(text, mode_args)
        else:
            # If the mode has changed, update the mode arguments and set the new mode
            mode_args = mode[1]
            mode = mode[0]
            # Print the new mode
            print(f"Mode has been set to {mode}")


if __name__ == '__main__':
    main()
