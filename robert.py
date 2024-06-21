import modes
import speech_recognition as sr
from helper import record_sample, change_mode, get_language

r = sr.Recognizer()
mode = "normal"
mode_args = ""

def main():
    global mode, mode_args
    print("Добро пожаловать. Всё настроено и готово")

    while True:
        if mode == "normal":
            language = 'ru'
        elif mode == "translate":
            language  = tuple[0]

        print("Recording...")
        try:
            text = record_sample(r, language)
        except sr.UnknownValueError:

            print("No audio provided")
            continue

        print(text)

        
        old_mode = mode
        mode = change_mode(mode, text)

        
        if mode[0] == old_mode:

            mode = mode[0]
            getattr(modes, mode)(text, mode_args)
        else:
            mode_args = mode[1]
            mode = mode[0]
            # Print the new mode
            print(f"Mode has been set to {mode}")


if __name__ == '__main__':
    main()
