#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.1.2"

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

def prevent_doubled_chars(text):
    text_as_list = list(text)
    for index in range(len(text_as_list)-1):
        if text_as_list[index] == text_as_list[index+1]:
            text_as_list[index+1] = "+"
    text = ''.join(text_as_list)
    return text

def recreate_doubled_chars(text):
    text_as_list = list(text)
    for index in range(len(text_as_list)-1):
        if text_as_list[index+1] == '+':
            text_as_list[index+1] = text_as_list[index]
    text = ''.join(text_as_list)
    return text

def encode(text):
    text = rot13(text)
    text = prevent_doubled_chars(text)
    text = replace_spaces(text)
    print(text)

def decode(text):
    text = rot13(text)
    text = recreate_doubled_chars(text)
    text = replace_numbers(text, string.digits)
    print(text)

def main():
    if len(sys.argv)>2:
        choice = str(sys.argv[1])
        text = str(sys.argv[2])
        
        if (choice == 'encode') and (len(sys.argv)>2):
            encode(text)
        elif (choice == 'decode') and (len(sys.argv)>2):
            decode(text)
    else:
        print("Please use 'decode' or 'encode' option :\n\n./sepyrot.py <decode/encode> \"<message>\"")


main()
