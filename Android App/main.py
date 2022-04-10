from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import HoverBehavior


# The Main/Home Screen
class HomeScreen(Screen):
    pass


# The Idea Log/Diary Screen
class IdeaLogScreen(Screen):
    pass


class CustomIconButton(MDCard, HoverBehavior):
    text = StringProperty()


class TestApp(MDApp):
    def build(self):
        self.root = Builder.load_file("design.kv")


if __name__ == '__main__':
    TestApp().run()