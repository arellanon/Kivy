#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:55:07 2021

@author: nahuel
"""
from kivy.app import App
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('test.kv')

class MyWidget(BoxLayout):
    pass
    
class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()