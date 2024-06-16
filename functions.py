from helper import get_normal_form
from consts import hello_aliases


def echo(text: str):
    return text


def exit_app():
    exit()


def hi(name: str) -> str:
    """
    This function greets the user with a personalized message.

    Args:
    name (str): The name of the person to be greeted.

    Returns:
    str: A personalized greeting message.

    The function first normalizes the input name using `get_normal_form(name)`.
    Then, it looks up the normalized name in the `hello_aliases` dictionary.
    If the name is found in the dictionary, it uses the corresponding value as the greeting.
    If the name is not found, it uses the original normalized name as the greeting.
    """
    form = get_normal_form(name)
    form = hello_aliases.get(form, form)
    return f"Привет, {form}"
