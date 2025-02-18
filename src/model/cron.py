import flet as ft
from time import sleep


class Chronometer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.time_text = None
        self.paused_time = False

    def start(self, page: ft.Page, time_text: ft.Text):
        self.time_text = time_text
        if self.paused_time is not True:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
        self.time_text.value = f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
        page.update()

    def pause(self, page: ft.Page):
        self.paused_time = True
        page.update()

    def stop(self, page: ft.Page, time_text: str):
        self.time_text = time_text
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.paused_time = True
        self.time_text.value = f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
        page.update()

    def set_pause(self):
        self.paused_time = False
