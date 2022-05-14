
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import platform
from kivy.lang import Builder

class MyGrid(Widget):
    pass

class BoxLayoutHangMan(BoxLayout):
    pass

class HangManApp(App):
    def build(self):
        
        #Image widget
        #self.window.add_widget(Image(source="hangman.png"))
        #self.greeting = Label(text="Will you hang?")
        #self.window.add_widget(self.greeting)

        #self.user = TextInput(multiline=False)
        #self.window.add_widget(self.user)


        return BoxLayoutHangMan()
HangManApp().run()