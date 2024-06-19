from helper import detect_command, remove_mention, say_text, translate as helper_translate, get_language
import functions


def normal(text: str, _) -> None:
    """
    Processes the input text and performs the following actions based on the detected mentions and commands.

    Args
    text (str): The input text to be processed.

    Returns
    None: The function does not return any value, as it performs actions on the input text and prints the corresponding output.

    The function first removes any mentions from the input text using the `remove_mention` function. 
    If no mentions are detected, the function prints a message indicating that no mention was found. 
    Then, the function detects any commands in the input text using the `detect_command` function. 
    If a command is detected, the function retrieves the corresponding function from the `functions` module 
    and calls it with the appropriate arguments. The function then prints the output of the called function. 
    If no command is detected, the function prints a message indicating that no command was found. 
    Finally, the function uses the `say_text` function to convert the output text to speech and play it 
    using the system's audio playback capabilities.
    """
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
    """
    Translates the input text from the specified source language to the specified target language 
    and plays the translated text using the system's audio playback capabilities.

    Args
    text (str): The input text to be translated.
    data (str): The input text containing the source and target languages.

    Returns
    None: The function does not return any value, as it performs the translation and plays the translated text 
    using the system's audio playback capabilities.

    The function first retrieves the source and target languages from the input text using the `get_language` function. 
    Then, it uses the `helper_translate` function to translate the input text from the specified source language 
    to the specified target language. Finally, the function uses the `say_text` function 
    to convert the translated text to speech and play it using the system's audio playback capabilities.
    """
    fl, tl = get_language(data)
    trans = helper_translate(text, fl, tl)
    say_text(trans, tl)
