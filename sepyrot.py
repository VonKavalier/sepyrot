#!/usr/bin/env python
"""Shebang."""
# -*- coding: utf-8 -*-

import string
import re
from random import randint
import codecs
import sys


__version__ = "1.1.3"


def replace_spaces(text):
    """Transform every space of the string into random number."""
    nb_spaces = text.count(' ')
    for i in range(nb_spaces):
        text = text.replace(' ', str(randint(0, 9)), 1)
    return text


def replace_numbers(text):
    """Transform every number of the string into space."""
    return re.sub('[%s]' % string.digits, ' ', text)


def rot13(text):
    """Apply rot13 encryption to given text."""
    text = codecs.encode(text, 'rot_13')
    return text


def prevent_doubled_chars(text):
    """Change second of doubled letter with a '+'."""
    text_as_list = list(text)
    for index in range(len(text_as_list) - 1):
        if text_as_list[index] == text_as_list[index + 1]:
            text_as_list[index + 1] = "+"
    text = ''.join(text_as_list)
    return text


def recreate_doubled_chars(text):
    """Transform '+' chars into previous letter."""
    text_as_list = list(text)
    for index in range(len(text_as_list) - 1):
        if text_as_list[index + 1] == '+':
            text_as_list[index + 1] = text_as_list[index]
    text = ''.join(text_as_list)
    return text


def encode(text):
    """Call the different encoding steps."""
    text = rot13(text)
    text = prevent_doubled_chars(text)
    text = replace_spaces(text)
    print(text)


def decode(text):
    """Call the different decoding steps."""
    text = rot13(text)
    text = recreate_doubled_chars(text)
    text = replace_numbers(text)
    print(text)


def main():
    """Entrance of the script."""
    if len(sys.argv) > 2:
        choice = str(sys.argv[1])
        text = str(sys.argv[2])

        if (choice == 'encode') and (len(sys.argv) > 2):
            encode(text)
        elif (choice == 'decode') and (len(sys.argv) > 2):
            decode(text)
    else:
        message = "Please use 'decode' or 'encode' option :"
        message += "\n\n./sepyrot.py <decode/encode> \"<message>\""
        print(message)


if __name__ == '__main__':
    main()
