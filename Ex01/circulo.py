# circulo.py

from forma import Forma

class Circulo(Forma):
    def __init__(self, raio, cor="black"):
        super().__init__(cor)
        self.raio = raio

    def desenhar(self):
        self.tartaruga.color(self.cor)
        self.tartaruga.begin_fill()
        self.tartaruga.circle(self.raio)
        self.tartaruga.end_fill()
