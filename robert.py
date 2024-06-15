import functions
import speech_recognition as sr
from helper import (
    record_sample, 
    detect_command, 
    detect_mention, 
    say_text
)
from consts import (
    names, 
    commands
)

r = sr.Recognizer()


def main():
    print("Добро пожаловать. Всё настроено и готово")
    while True:
        print("Recording...")
        try:
            text = record_sample(r)
        except sr.UnknownValueError:
            print("No audio provided")
            continue

        print(text)

        if not detect_mention(text):
            print("No mention")
            continue

        command = detect_command(text)
        if command is None:
            print("No command")
            continue

        print(f"Coomand named {command} found")
        output = getattr(functions, command)(text)
        print(f"Output: {output}")

        if output is None:
            print("No output")
            continue
        say_text(output)



if __name__ == '__main__':
    main()
