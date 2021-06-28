#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:16:44 2021

@author: nahuel
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.button import Button

# Designate Our .kv design file
Builder.load_file('animations.kv') 

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}


class MyLayout(BoxLayout):
    def __init__(self):
        super(MyLayout,self).__init__()             
        self.Box1 = Wid_Box1()
        self.add_widget(self.Box1)
        self.Box2 = Wid_Box2()
        self.add_widget(self.Box2)
        #self.Box1.Btn.bind(on_press = self.add_plot )
    
class Wid_Box1(BoxLayout):
    pass
"""
    def __init__(self):
        super(Wid_Box1, self).__init__()
        self.left = Widget( background_color =(1, 1, 1, 1) )
        self.add_widget( self.left )
        #self.Btn = Button(text="Start")
        #self.add_widget(self.Btn)
"""     

class Wid_Box2(BoxLayout):
    pass

class LeftRect(Widget):
    pass

class RightRect(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    reset()
    AwesomeApp().run()