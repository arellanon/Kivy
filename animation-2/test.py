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
        wid_left = self.ids.left
        animate = Animation( height = 200, duration=.5)
        animate += Animation( height = 100, duration=.5)
        animate.start(wid_left)
        
        
        #animate.bind(on_complete=self.on_anim1_complete,
                #on_progress=self.on_anim1_progress)
        
        """
        wid_right = self.ids.right
        animate2 = Animation( height = 200, duration=.5)
        animate2 += Animation( height = 100, duration=.5)
        animate2.start(wid_right)
        
        animate.on_complete(print("hola mundo"))
        """

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
"""

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    reset()
    TestApp().run()