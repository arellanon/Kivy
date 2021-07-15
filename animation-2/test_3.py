#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:08:56 2021

@author: nahuel
"""
from kivy.animation import Animation, Sequence, Parallel
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class MySequence(Sequence):
    widgets = ListProperty([])

    def start(self, widget):
        super(MySequence, self).start(widget)
        self.widgets.append(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)

class MyParallel(Parallel):
    widgets = ListProperty([])

    def start(self, widget):
        super(MyParallel, self).start(widget)
        self.widgets.append(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)

class MyAnim(Animation):
    widgets = ListProperty([])

    def start(self, widget):
        super(MyAnim, self).start(widget)
        self.widgets.append(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)


class TestApp(App):
    def animate(self, instance):
        
        #print(self.ids)
        self.animation = MyAnim(pos=(200, 200), d=5)
        self.animation.on_complete = self.completed
        # sequential
        #self.animation += MyAnim(pos=(400, 400), t='out_sine')
        
        # parallel
        #self.animation &= MyAnim(size=(200, 300), d=5)
        #Clock.schedule_once(self.another_anim, 1)
        
        self.animation.start(instance)

    """
    def another_anim(self, dt):
        self.animation.start(self.label)
    """

    def completed(self, widget):
        print('Animation completed - animated Widget:', widget)
        Clock.schedule_once(self.check_anim, 2)

    def check_anim(self, dt):
        print(dt, 'seconds after Animation completed - animated Widgets:', self.animation.widgets)

    def build(self):
        fl = FloatLayout()
        self.button = Button(id="btn1", size_hint=(None, None), size=(100,50), pos=(0,0), text='click here', on_press=self.animate)
        fl.add_widget(self.button)
        self.label = Label(text='label', size_hint=(None, None), size=(100, 500), pos=(400, 200))
        fl.add_widget(self.label)
        return fl

if __name__ == '__main__':
    TestApp().run()