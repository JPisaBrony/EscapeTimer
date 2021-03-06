from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time

class MainLayout(BoxLayout):
    countdown_timer = 60 * 1000
    counter = StringProperty("00:%02d" % (countdown_timer / 1000))
    started_time = 0
    state = 0

    def count_down(self):
        if self.state == 0:
            self.started_time = int(round(time.time() * 1000))
            Clock.schedule_interval(self.update_countdown, 0.1)
            self.ids.start.text = "Reset Countdown"
            self.state = 1
        elif self.state == 1:
            Clock.unschedule(self.update_countdown)
            self.started_time = 0
            self.countdown_timer = 60 * 1000
            self.counter = "00:%02d" % (self.countdown_timer / 1000)
            self.ids.start.text = "Start Countdown"
            self.state = 0

    def update_countdown(self, dt):
        cur_time = int(round(time.time() * 1000))
        timer_time = cur_time - self.started_time
        mill = self.countdown_timer - timer_time
        sec, mil = divmod(mill, 1000)
        min, sec = divmod(sec, 60)
        self.counter = "%02d:%02d" % (min, sec)

    def add_time(self):
        self.countdown_timer += 1000

class EscapeTimer(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    EscapeTimer().run()
