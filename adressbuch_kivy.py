from pydblite import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.instructions import Canvas
from kivy.uix.boxlayout import *

database = Base('adressbuch.pdl')
database.create('Vorname', 'Nachname', 'Telefon_Nummer', 'Adresse', mode="open")

class ClearApp(App):

    def build(self):
        self.site = self.box = BoxLayout(orientation="vertical")
        self.box = BoxLayout(orientation='horizontal', minimum_height=(.4,2))
        self.txt = TextInput(hint_text='Vorname', size_hint=(.4,.2))
        self.txt2 = TextInput(hint_text='Nachname', size_hint=(.4,.2))
        self.txt3 = TextInput(hint_text='Adresse', size_hint=(0.1,.1))
        self.txt4 = TextInput(hint_text='Telefon Nummer', size_hint=(0.1,.1))
        self.btn = Button(text='Hinzufügen', on_press=self.submit, size_hint=(.5,.1))
        self.box.add_widget(self.txt)
        self.box.add_widget(self.txt2)
        self.box.add_widgetself.txt3)
        self.box.add_widget(self.txt4)
        for i in db:
            self.site.add_widget(Label(text=f"Vorname={i['Vorname']}  Nachname={i['Nachname']}  Telefon={i['Telefon_nummer']  Adresse={i['Adresse']}", size_hint=(1,.1)))
        self.site.add_widget(self.box)

        return self.site

ClearApp().run()
