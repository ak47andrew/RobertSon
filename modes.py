from helper import detect_command, detect_mention, say_text, translate as helper_translate
import functions

def normal(text: str):
    if not detect_mention(text):
        print("No mention")
        return

    command = detect_command(text)
    if command is None:
        print("No command")
        return

    print(f"Coomand named {command} found")
    output = getattr(functions, command)(text)
    print(f"Output: {output}")

    if output is None:
        print("No output")
        return
    say_text(output)


def translate(text: str):
    trans = helper_translate(text, "ru", "en")
    say_text(trans, "en")
