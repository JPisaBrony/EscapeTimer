from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from multiprocessing import Manager
import server

class Window(BoxLayout):
    msg = []

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
        server.main(m)
        w.startup(m)
        return w

if __name__ == '__main__':
    ControlPanel().run()