#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:55:07 2021

@author: nahuel
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

kv_string = '''
<MyWidget>:
    Widget:
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        size_hint: 0.2, 0.2
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size
                pos: self.pos
    Widget:
        pos_hint: {'center_y': 0.5, 'center_x': 0.2}
        size_hint: 0.2, 0.2
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size
                pos: self.pos
    Widget:
        pos_hint: {'center_y': 0.5, 'center_x': 0.8}
        size_hint: 0.2, 0.2
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size
                pos: self.pos
    Widget:
        pos_hint: {'center_y': 0.2, 'center_x': 0.5}
        size_hint: 0.2, 0.2
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size
                pos: self.pos
    Widget:
        pos_hint: {'center_y': 0.8, 'center_x': 0.5}
        size_hint: 0.2, 0.2
        canvas:
            Color:
                rgb: 0.1, 0.6, 0.3
            Rectangle:
                size: self.size
                pos: self.pos
'''

Builder.load_string(kv_string)

class MyWidget(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()