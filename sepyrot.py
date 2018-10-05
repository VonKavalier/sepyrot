#!/usr/bin/env python
"""Shebang."""
# -*- coding: utf-8 -*-

import string
import re
from random import randint
import codecs
import sys
import getopt

__version__ = "1.1.4"


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


def main(argv):
    """Entrance of the script."""
    try:
        opts, args = getopt.getopt(
            argv,
            "he:d:",
            [
                "encode=",
                "decode="
            ]
        )
    except getopt.GetoptError as e:
        print(str(e))
        print('usage: sepyrot.py -e \"message to encode\"                  # encode a simple text')
        print('                  -d \"message to decode\"                  # decode a simple text\n')
        print('       sepyrot.py -e \"$(cat file.txt)\" > encoded_file.txt # encode a file')
        print('                  -d \"$(cat encoded_file.txt)\"            # decode a file')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: sepyrot.py -e \"message to encode\"                  # encode a simple text')
            print('                  -d \"message to decode\"                  # decode a simple text\n')
            print('       sepyrot.py -e \"$(cat file.txt)\" > encoded_file.txt # encode a file')
            print('                  -d \"$(cat encoded_file.txt)\"            # decode a file')
            sys.exit()
        elif opt in ("-e", "--encode"):
            encode(arg)
        elif opt in ("-d", "--decode"):
            decode(arg)

if __name__ == '__main__':
    main(sys.argv[1:])
