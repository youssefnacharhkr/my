import kivy
from kivy.app import App as A
from kivy.uix.widget import Widget as W
from kivy.uix.label import Label as L
from kivy.uix.textinput import TextInput as Ti
from kivy.uix.button import Button as B
from kivy.uix.image import Image as I
from kivy.core.window import Window

class ProgramziYn(A):
    def build(self):
        self.w = W()
        self.colorsf = "#171810"
        Window.clearcolor = (self.colorsf)
        self.image = 'ProgrAmziYn.png'
        self.logo = I(source=self.image, x=350, top=560,)
        self.w.add_widget(self.logo)
        self.username = L(text="Username", color="white", font_size="20", y=360, x=150)
        self.w.add_widget(self.username)
        self.user_inpt = Ti(x=250, y=390, width=200, height=30, font_size=15, multiline=False)
        self.w.add_widget(self.user_inpt)
        return self.w

if __name__ == "__main__":
    ProgramziYn().run()