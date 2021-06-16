#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:19:55 2020

@author: nahuel
"""

"""
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__':
    myApp().run()
"""    
    
    
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
   def build(self):
      return Button(text='Hello World')

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

if __name__ == '__main__':
   reset()
   TestApp().run()