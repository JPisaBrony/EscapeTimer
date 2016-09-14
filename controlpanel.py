from server import Server
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from multiprocessing import Manager

class Window(BoxLayout):
    def startup(self, m):
	    self.msg = m

    def count_down(self):
        self.msg[0] = "start"
	
    def add_time(self):
        pass

class ControlPanel(App):
    def build(self):
        w = Window()
        man = Manager()
        m = man.list()
        s = Server('127.0.0.1', 3000, m)
        s.start()
        w.startup(m)
        return w

if __name__ == '__main__':
    ControlPanel().run()