from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.Builder import Builder

Builder.load_file("menu.kv")

class MainWidget(relativelayout):
    pass

class TheLabApp(App):
    pass


TheLabApp().run()