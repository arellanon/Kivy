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
#import time
#from kivy.uix.widget import Widget
#from kivy.properties import ListProperty
#from kivy.graphics import Color, Ellipse, Line
#from kivy.clock import Clock
#from kivy.core.window import Window

Builder.load_file('test_4.kv')
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
#        print( )
        #self.ids.bar.canvas.add( Color( 0, 1, 0) )
        self.my_animation(self.ids.bar)
        #self.my_animation(self.ids.right)
        #animate.bind(on_complete= self.my_callback )
        
    def my_animation(self, in_widget, *args):
        animate = Animation(width = 400, duration=1)
        animate += Animation(animated_color=(0,0,1) )
        #animate += Animation( background_color =(1, 1, 1, 1), duration=3)
        animate += Animation(width = 0, duration=1)
        animate.start(in_widget)

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    reset()
    TestApp().run()