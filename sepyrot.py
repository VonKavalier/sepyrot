#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0.1"

from random import randint
import codecs
import sys
import re, string

def replace_spaces(text):
    nb_spaces = text.count(' ')
    for i in range(nb_spaces):
        text = text.replace(' ', str(randint(0, 9)), 1)
    return text

def replace_numbers(s, chars):
    return re.sub('[%s]' % chars, ' ', s)

def rot13(text):
    text = codecs.encode(text, 'rot_13')
    return text

def encode(text):
    text = rot13(text)
    text = replace_spaces(text)
    print(text)

def decode(text):
    text = rot13(text)
    text = replace_numbers(text, string.punctuation+string.digits)
    print(text)

def main(text):
    choice = str(sys.argv[1])

    if choice == 'encode':
        encode(text)
    elif choice == 'decode':
        decode(text)
    else:
        print("Please use 'decode' or 'encode' option : setpy <decode/encode> \"<message>\"")

text = str(sys.argv[2])

main(text)
