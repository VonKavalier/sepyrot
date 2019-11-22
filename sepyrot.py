#!/usr/bin/env python
"""Shebang."""
# -*- coding: utf-8 -*-

import string
import re
from random import randint
import codecs
import sys
import getopt

__version__ = "1.1.5"


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
    sys.exit()


def decode(text):
    """Call the different decoding steps."""
    text = rot13(text)
    text = recreate_doubled_chars(text)
    text = replace_numbers(text)
    print(text)
    sys.exit()

def show_help():
    print('\nusage: -e \"message to encode\"                  # encode a simple text')
    print('       -d \"message to decode\"                  # decode a simple text\n')
    print('       -e \"$(cat file.txt)\" > encoded_file.txt # encode a file')
    print('       -d \"$(cat encoded_file.txt)\"            # decode a file')
    sys.exit(2)

def main(argv):
    """Entrance of the script."""
    try:
        opts, args = getopt.getopt(
            argv,
            "e:d:",
            [
                "encode=",
                "decode="
            ]
        )
    except getopt.GetoptError as e:
        print(str(e))
        show_help()
    for opt, arg in opts:
        if opt in ("-e", "--encode"):
            encode(arg)

        if opt in ("-d", "--decode"):
            decode(arg)

    show_help()

if __name__ == '__main__':
    main(sys.argv[1:])
