#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:24:45 2021

@author: nahuel
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
#from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('progress.kv')

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

class MyLayout(Widget):
    def press_it(self):
        current = self.ids.my_progress_bar.value
        if current == 1:
            current = 0
        current+= .25
        self.ids.my_progress_bar.value = current
        self.ids.my_label.text = f'{int(current*100)} % Progress' 
    
        
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    reset()
    AwesomeApp().run()