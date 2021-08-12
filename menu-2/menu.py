#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:48:16 2021

@author: nahuel
"""
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

#Define our different screens
class MenuWindow(Screen):
    pass

class CalibracionWindow(Screen):
    pass

class MachineLearningWindow(Screen):
    pass

class RealtimeWindow(Screen):
    pass

class ConfiguracionCalibracionWindow(Screen):
    pass

class StartCalibracionWindow(Screen):
    
    def animate_it(self, *args):
        #print("Print: ", self.ids.bar)
        self.my_animation(self.ids.bar)
        
    def my_animation(self, in_widget, *args):
        self.time_trial = 8
        self.run_n = 2
        self.trial_per_run = 10
        self.time_pause = 10
        
        animate = Animation()        
        for i in range(self.run_n):
            print('\nCorrida N#: ', i)
            #Se crea lista de stack
            stack = []
            left  = [0] * (self.trial_per_run // 2)
            rigth = [1] * (self.trial_per_run // 2)
            stack = left + rigth
            #print(stack)
            random.shuffle(stack)
            print(stack)
            for x in stack:
                if x == 0:
                    animate = self.izquierda(animate)
                else:
                    animate = self.derecha(animate)
            animate = self.pausa(animate)
        animate.start(in_widget)
        
    def derecha(self, animate):
        animate += Animation(animated_color=(0,0,1) )
        animate += Animation( size_hint_x = 0.7, duration=self.time_trial//2 )
        animate += Animation( size_hint_x = 0, duration=self.time_trial//2 )
        return animate
    
    def izquierda(self, animate):
        animate += Animation(animated_color=(1,0,0) )
        animate += Animation( size_hint_x = -0.7, duration=self.time_trial//2 )
        animate += Animation( size_hint_x = 0, duration=self.time_trial//2 )
        return animate
    
    def pausa(self, animate):
        animate += Animation(animated_color=(0,0,1), duration=self.time_pause)
        print("pausa: ", self.time_pause)
        return animate


class WindowManager(ScreenManager):
    pass

#Designate Our .kv design file
kv = Builder.load_file('menu.kv')

class AwesomeApp(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    reset()
    AwesomeApp().run()