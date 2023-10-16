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

Builder.load_file("widget_examples.kv")

class WidgetExample(GridLayout):
    count = 0
    count_enable = BooleanProperty(False)
    my_text = StringProperty("HAHA")
    # slider_value_text = StringProperty("value")
    text_input_str = StringProperty("I")
    
    def on_button_click(self):
        print("Button clicked")
        if (self.count_enable):
            self.count = self.count + 1    #self.count += 1
            self.my_text = str (self.count)
    
    def on_toggle_button_state(self, widget):
        print("toggle " + widget.state)
        if(widget.state == "normal"):
            print("yaa normal")
            widget.text = "OFF"
            self.count_enable = False
        elif(widget.state == "down"):
            print("yaa oke nyala")
            widget.text = "ON"
            self.count_enable = True

    def on_switch_active(self, widget):
        print("switch " + str(widget.active))

    def on_slider_value(self, widget):
        print("slider : " + str(int(widget.value)))
        # self.slider_value_text = str(int(widget.value))

    def on_text_validate(self, widget):
        print("text input: " + widget.text)
        self.text_input_str = widget.text

# class PageLayoutExample(PageLayout):
    # pass

# class ScrollViewExample(ScrollView):
    #pass