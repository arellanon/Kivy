#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:51:23 2021

@author: nahuel
"""
import matplotlib
import matplotlib.pyplot as plt 
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import numpy as np

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
            
def run_plot():
    #matplotlib en segundo plano
    matplotlib.use('Agg')
    
    """
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
        plt.pause(0.1)
     

    """
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

class MyApp(App):
    def build(self):
        box = BoxLayout()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return box

if __name__ == '__main__':
    reset()
    run_plot()
    MyApp().run()