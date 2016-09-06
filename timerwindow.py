from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from multiprocessing import Process, Manager
import time
import socket

class Connection():
    def start(self, m):
        HOST = '127.0.0.1'
        PORT = int(3000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        m.append("")
        while True:
            data = s.recv(1024)
            if not data:
                break
            m[0] = data
            s.send(data)
        s.close()

class Window(BoxLayout):
    countdown_timer = 60 * 1000
    counter = StringProperty("00:%02d" % (countdown_timer / 1000))
    started_time = 0
    state = 0
    msg = ""
    
    def startup(self, m):
        self.msg = m
        Clock.schedule_interval(self.check_msg, 0.01)
    
    def check_msg(self, dt):
        if self.msg[0] == "start":
            self.count_down()
        self.msg[0] = ""

    def count_down(self):
        if self.state == 0:
            self.started_time = int(round(time.time() * 1000))
            Clock.schedule_interval(self.update_countdown, 0.1)
            self.state = 1
        elif self.state == 1:
            Clock.unschedule(self.update_countdown)
            self.started_time = 0
            self.countdown_timer = 60 * 1000
            self.counter = "00:%02d" % (self.countdown_timer / 1000)
            self.state = 0

    def update_countdown(self, dt):
        cur_time = int(round(time.time() * 1000))
        timer_time = cur_time - self.started_time
        mill = self.countdown_timer - timer_time
        sec, mil = divmod(mill, 1000)
        min, sec = divmod(sec, 60)
        self.counter = "%02d:%02d" % (min, sec)

class TimerWindow(App):
    def build(self):
        w = Window()
        c = Connection()
        man = Manager()
        m = man.list()
        p = Process(target=c.start, args=(m,))
        p.start()
        w.startup(m)
        return w

if __name__ == '__main__':
    TimerWindow().run()
