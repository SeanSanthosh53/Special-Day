import kivy
from kivymd.app import MDApp
from kivy.lang import Builder


class TestApp(MDApp):
    def build(self): 
        self.root = Builder.load_file("design.kv")


if __name__ == '__main__':
    TestApp().run()