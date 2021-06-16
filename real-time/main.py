"""Real time plotting of Microphone level using kivy
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
#from threading import Thread
import threading
import audioop
import pyaudio

Builder.load_file('look.kv')

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    print(EventLoop.event_listeners)
    if not EventLoop.event_listeners:
        print("ENTRO")
        from kivy.cache import Cache
        window.Window.clear()
        window.Window = window.core_select_lib('window', window.window_impl, True)
        print("children: ", window.Window.children)
        #Cache.print_usage()
        #print(Cache._objects)
        for cat in Cache._categories:
            Cache._objects[cat] = {}
            #print(cat)
        #window.Window.fullscreen=True
        print(Cache._objects)

class Microphone (threading.Thread):
    def __init__ (self):
        threading.Thread.__init__ (self)
        self.keep_alive = True

    def run(self):
        chunk = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
    
        s = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=chunk)
        global levels
        while self.keep_alive:
            data = s.read(chunk)
            mx = audioop.rms(data, 2)
            #print(mx)
            if len(levels) >= 100:
                levels = []
            levels.append(mx)


class Logic(BoxLayout):
    def __init__(self,):
        super(Logic, self).__init__()
        #self.clear_widgets()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/5) for i, j in enumerate(levels)]


class RealTimeMicrophone(App):
    def build(self):
        #self.canvas.clear()
        out = Logic()
        #out.clear_widgets()
        return out
        #return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Microphone()
    get_level_thread.start()
    reset()
    RealTimeMicrophone().run()
    get_level_thread.keep_alive = False
    get_level_thread.join()