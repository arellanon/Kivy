#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:12:07 2021

@author: nahuel
"""
import kivy
#kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
#from kivy.lang import Builder

#from kivy.config import Config

def run_plot():
    #matplotlib en segundo plano
    matplotlib.use('Agg')
    x1=[1,2,3,4,5,6]
    y1=[4,3,5,6,7,4]
    
    x2=[1,2,3,4,5,6]
    y2=[8,6,10,12,14,8]
    
    fig=plt.figure()
    subplot1=fig.add_subplot(2,1,1)
    subplot1.plot(x1,y1)
    
    subplot2=fig.add_subplot(2,1,2)
    subplot2.plot(x2,y2)
    fig.suptitle("Add subplots to a figure")
    
    
def run_plot2():
    matplotlib.use('Agg')
    plt.style.use("ggplot")
    plt.axis([0, 100, 0, 1])
    plt.ion()
    
    xs = [0, 0]
    ys = [1, 1]
    
    for i in range(100):
        y = np.random.random()
        xs[0] = xs[1]
        ys[0] = ys[1]
        xs[1] = i
        ys[1] = y
        plt.plot(xs, ys)
        #plt.pause(0.1)

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}

class Wid_Alfa(BoxLayout):
    def __init__(self):
        super(Wid_Alfa,self).__init__()
        self.Box1 = Wid_Box1()
        self.Box2 = Wid_Box2()
        self.add_widget(self.Box1)
        self.add_widget(self.Box2)
        
        self.Box1.Btn.bind(on_press = self.add_plot )
    
    def add_plot(self, *arg):
        run_plot2()
        self.Box2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class Wid_Box1(BoxLayout):
    def __init__(self):
        super(Wid_Box1, self).__init__()
        self.Btn = Button(text="Start")
        self.add_widget(self.Btn)

class Wid_Box2(BoxLayout):
    pass

class  MainApp(App):
    def build(self):
        return Wid_Alfa()
    
if __name__ == '__main__':
    reset()
    MainApp().run()