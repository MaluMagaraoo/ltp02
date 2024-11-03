# forma.py

from turtle import Turtle

class Forma:
    def __init__(self, cor="black"):
        self.cor = cor
        self.tartaruga = Turtle()

    def desenhar(self):
        raise NotImplementedError("Método 'desenhar' deve ser implementado na subclasse.")

    def limpar(self):
        self.tartaruga.clear()
