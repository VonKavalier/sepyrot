#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import string
import sys
from random import randint

import wx

__version__ = "1.1.2"


class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        text = 'Oui bonjour toi'
        text_encoded = self.encode(text)
        self.encode_form = wx.TextCtrl(pnl, pos=(25, 25), size=(250, 25), name="decoded_form")

        self.encode_button = wx.Button(pnl, label="Encode", pos=(25, 60))

        self.decode_form = wx.TextCtrl(pnl, name="encoded_form", pos=(25, 85), size=(250, 25))

        # and a status bar
        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.on_encode, self.encode_button)

    def on_exit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def on_hello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def on_encode(self, event):
        wx.decode_form.SetValue(wx.encode(wx.encode_form.GetValue()))
        self.decode_form = wx.TextCtrl(pnl, name="encoded_form", pos=(25, 85), size=(250, 25), value=wx.encode('test'))

    def replace_spaces(self, text):
        nb_spaces = text.count(' ')
        for i in range(nb_spaces):
            text = text.replace(' ', str(randint(0, 9)), 1)
        return text

    def replace_numbers(self, chars):
        return re.sub('[%s]' % chars, ' ', self)

    def rot13(self, text):
        text = codecs.encode(text, 'rot_13')
        return text

    def prevent_doubled_chars(self, text):
        text_as_list = list(text)
        for index in range(len(text_as_list) - 1):
            if text_as_list[index] == text_as_list[index + 1]:
                text_as_list[index + 1] = "+"
        text = ''.join(text_as_list)
        return text

    def recreate_doubled_chars(self):
        text_as_list = list(self)
        for index in range(len(text_as_list) - 1):
            if text_as_list[index + 1] == '+':
                text_as_list[index + 1] = text_as_list[index]
        self = ''.join(text_as_list)
        return self

    def encode(self, text):
        text = self.rot13(text)
        text = self.prevent_doubled_chars(text)
        text = self.replace_spaces(text)
        return text

    def decode(self):
        self = wx.rot13(self)
        self = wx.recreate_doubled_chars(self)
        self = wx.replace_numbers(self, string.digits)
        print(self)

    def main():
        if len(sys.argv) > 2:
            choice = str(sys.argv[1])
            text = str(sys.argv[2])

            if (choice == 'encode') and (len(sys.argv) > 2):
                wx.encode(text)
            elif (choice == 'decode') and (len(sys.argv) > 2):
                wx.decode(text)
        else:
            print("Please use 'decode' or 'encode' option :\n\n./sepyrot.py <decode/encode> \"<message>\"")

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='sepyrot GUI')
    frm.Show()
    app.MainLoop()
