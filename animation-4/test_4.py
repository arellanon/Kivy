#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:55:07 2021

@author: nahuel
"""
import random
import time
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.animation import Animation


Builder.load_file('test_4.kv')

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
        self.my_animation(self.ids.bar)
        
    def my_animation(self, in_widget, *args):
        self.time_trial = 8
        self.run_n = 2
        self.trial_per_run = 10
        self.time_pause = 3
        
        
        for i in range(self.run_n):
            print('\nCorrida N#: ', i)
            #Se crea lista de stack
            stack = []
            left  = [0] * (self.trial_per_run // 2)
            rigth = [1] * (self.trial_per_run // 2)    
            stack = left + rigth
            print(stack)
            random.shuffle(stack)
            print(stack)
            animate = Animation()
            for x in stack:
                #time.sleep(self.time_pause)
                """
                ts = time.time()
                print()
                print(x, ' ', ts, ' - ', datetime.fromtimestamp(ts))
                label=np.array( [ [ts], [x] ] )
                if labels is None:
                    labels = label
                else:
                    labels = np.append(labels, label, axis=1)
                    
                os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq)) #beep
                """
                #for j in range(self.time_trial):
                if x == 0:
                    animate = self.izquierda(animate)
                else:
                    animate = self.derecha(animate)    
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

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    reset()
    TestApp().run()