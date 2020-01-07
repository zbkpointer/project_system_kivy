import kivy
kivy.require('1.11.1')
from kivy.config import Config
print(Config.get('kivy','default_font'))
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()