#this is for logical code

import os
os.environ['KIVY_IMAGE'] = 'sdl2,gif'
import kivy
from kivy.loader import Loader
from typing import Text
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.lang import Builder
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from navigation_screen_manager import NavigationScreenManager

class MyScreenManager(NavigationScreenManager):
    pass

class thelabApp(App):
    # pass
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager

thelabApp().run()