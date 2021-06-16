#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:24:45 2021

@author: nahuel
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
#from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import time

Builder.load_file('plot_3.kv')

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
    fig=plt.figure()
    plt.ion()
    
    subplot1=fig.add_subplot(2,1,1)
    subplot1.axis([0, 100, 0, 1])
    
    xs = [0, 0]
    ys = [1, 1]
    
    for i in range(100):
        y = np.random.random()
        xs[0] = xs[1]
        ys[0] = ys[1]
        xs[1] = i
        ys[1] = y
        subplot1.plot(xs, ys)

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
    def press_it(self):
        #run_plot2()
        matplotlib.use('Agg')
        fig=plt.figure()
        plt.ion()
        
        subplot1=fig.add_subplot(2,1,1)
        subplot1.axis([0, 10, 0, 1])
        
        xs = [0, 0]
        ys = [1, 1]
        
        for i in range(10):
            y = np.random.random()
            xs[0] = xs[1]
            ys[0] = ys[1]
            xs[1] = i
            ys[1] = y
            subplot1.plot(xs, ys)
            
            f = FigureCanvasKivyAgg( plt.gcf() )
            self.ids.my_box2.clear_widgets()
            self.ids.my_box2.add_widget(f)
            
            #plt.pause(0.1)
            print("1")
        time.sleep(1)
        print("sali del loop")
        time.sleep(1)
        
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    reset()
    AwesomeApp().run()