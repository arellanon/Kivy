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
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.core.window import Window

Builder.load_file('test.kv')
#Builder.load_string(kv_string)

class MyWidget(FloatLayout):
    def __init__(self,):
        super(MyWidget, self).__init__()
        print( "TestPanel ids:", self.ids)
        
        
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0,0,1,1),
            duration=3)
        
        animate += Animation( height = 200,
                              duration=.5)        
        
        print(self.ids.left.height)
        self.ids.left.height+=0.1
        #self.ids.left.size_hint["x"] += 0.1 
#        pos_hint["x"] += 0.1
        #print( "out: ", self.ids['wid1'] )
        
        # Start the animation
        animate.start(widget)
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
class left(Widget):
    velocity = ListProperty([10, 15])

    def __init__(self, **kwargs):
        super(left, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60.)

    def update(self, *args):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x < 0 or (self.x + self.width) > Window.width:
            self.velocity[0] *= -1
        if self.y < 0 or (self.y + self.height) > Window.height:
            self.velocity[1] *= -1


class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()