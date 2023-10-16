import os
os.environ['KIVY_IMAGE'] = 'sdl2,gif'
import kivy
from kivy.loader import Loader
from typing import Text
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
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

Builder.load_file("layout_examples.kv")

class StackLayoutExample(StackLayout):
    #pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation: "rl-tb"
        for i in range(0, 100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))  #size=(dp(100), dp(100))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        self.add_widget(b1)
        self.add_widget(b2)
"""

class MainWidget(Widget):
    pass