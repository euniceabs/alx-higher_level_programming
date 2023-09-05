#!/usr/bin/python3


def text_indentation(text):
    """
    this function prints two new lines after each
    occurrence of '.', '?', and ':' chars.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    indented_lines = []

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuation_chars:
            indented_lines.append(current_line.strip())
            current_line = ""

    if current_line:
        indented_lines.append(current_line.strip())

    print("\n\n".join(indented_lines))
