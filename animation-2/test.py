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

Builder.load_file('test.kv')
#Builder.load_string(kv_string)

class MyWidget(FloatLayout):
    def __init__(self,):
        super(MyWidget, self).__init__()
        print( "TestPanel ids:", self.ids)
"""    
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,0,1,1),
            duration=3)
        
#        self.ids.left.pos_hint["x"] += 0.1 
#        pos_hint["x"] += 0.1
        print( "TestPanel ids:", self.ids.wid1)
        
        # Start the animation
        animate.start(widget)
"""
class Wid1(FloatLayout):
    pass

class Wid2(FloatLayout):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,0,1,1),
            duration=3)
        
#        self.ids.left.pos_hint["x"] += 0.1 
#        pos_hint["x"] += 0.1
        #print( "out: ", self.ids['wid1'] )
        
        # Start the animation
        animate.start(widget)

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()