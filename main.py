""" Gestion des imports"""
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

""" Version de kivy"""
kivy.require('2.2.0')

""" Creation et initialisation de la class GameView"""


class GameView(BoxLayout):
    def __int__(self):
        super(GameView, self).__init__()


""" Creation et initialisation de la class TestApp1"""


class TestApp1(App):
    def build(self):
        return GameView()


""" Creation d'une instance de testApp1"""
testApp1 = TestApp1()

""" Lancement de instance avec run"""
testApp1.run()
