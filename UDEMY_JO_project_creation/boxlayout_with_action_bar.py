from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

Builder.load_file("boxlayout_with_action_bar.kv")

class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()