import modes
import speech_recognition as sr
from helper import record_sample


r = sr.Recognizer()
mode = "translate"


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

        getattr(modes, mode)(text)



if __name__ == '__main__':
    main()
