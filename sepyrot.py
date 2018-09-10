#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import string
import sys
from random import randint

import wx

__version__ = "2.0.0"


class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        self.encode_form = wx.TextCtrl(pnl, pos=(25, 25), size=(250, 25), name="decoded_form", value="Text to encode")

        self.encode_button = wx.Button(pnl, label="Encode", pos=(25, 60))
        self.decode_button = wx.Button(pnl, label="Decode", pos=(150, 60))

        self.decode_form = wx.TextCtrl(pnl, name="encoded_form", pos=(25, 85), size=(250, 25), value="Text to decode")

        # and a status bar
        self.CreateStatusBar()

        self.Bind(wx.EVT_BUTTON, self.on_encode, self.encode_button)
        self.Bind(wx.EVT_BUTTON, self.on_decode, self.decode_button)

    def on_encode(self, event):
        self.decode_form.SetValue(self.encode(self.encode_form.GetValue()))

    def on_decode(self, event):
        self.encode_form.SetValue(self.decode(self.decode_form.GetValue()))

    def replace_spaces(self, text):
        nb_spaces = text.count(' ')
        for i in range(nb_spaces):
            text = text.replace(' ', str(randint(0, 9)), 1)
        return text

    def replace_numbers(self, text, chars):
        return re.sub('[%s]' % chars, ' ', text)

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

    def recreate_doubled_chars(self, text):
        text_as_list = list(text)
        for index in range(len(text_as_list) - 1):
            if text_as_list[index + 1] == '+':
                text_as_list[index + 1] = text_as_list[index]
        text = ''.join(text_as_list)
        return text

    def encode(self, text):
        text = self.rot13(text)
        text = self.prevent_doubled_chars(text)
        text = self.replace_spaces(text)
        return text

    def decode(self, text):
        text = self.rot13(text)
        text = self.recreate_doubled_chars(text)
        text = self.replace_numbers(text, string.digits)
        return text


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='sepyrot GUI')
    frm.Show()
    app.MainLoop()
