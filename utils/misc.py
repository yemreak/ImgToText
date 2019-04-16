import json


def prettify(text: str):
    final_word: str = ""
    words = text.split()

    for word in words:
        final_word += word + " "

    return final_word.replace(". ", ".\n")


def parse_text(text: str):
    author = text.split(".")[-1]
    text = text.replace(author, "")
    return text, author
