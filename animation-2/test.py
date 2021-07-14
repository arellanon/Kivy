#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:55:07 2021

@author: nahuel
"""
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.animation import Animation
import time
#from kivy.uix.widget import Widget
#from kivy.properties import ListProperty
#from kivy.clock import Clock
#from kivy.core.window import Window

Builder.load_file('test.kv')
#Builder.load_string(kv_string)

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

class MyWidget(FloatLayout):
    def __init__(self,):
        super(MyWidget, self).__init__()
        
    def animate_it(self, *args):
        #wid_left = self.ids.left
        self.my_animation(self.ids.left)
        self.my_animation(self.ids.right)
        #animate.bind(on_complete= self.my_callback )
        
    def my_animation(self, in_widget, *args):
        animate = Animation(height = 200, duration=.5)
        animate += Animation(height = 100, duration=.5)
        animate.start(in_widget)
        
"""
    def my_callback(self, in_widget, *args):
        #wid_right = in_widget
        animate2 = Animation( height = 200, duration=.5)
        animate2 += Animation( height = 100, duration=.5)
        animate2.start(in_widget)
"""

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    reset()
    TestApp().run()