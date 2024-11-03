# quadrado.py

from forma import Forma

class Quadrado(Forma):
    def __init__(self, lado, cor="black"):
        super().__init__(cor)
        self.lado = lado

    def desenhar(self):
        self.tartaruga.color(self.cor)
        self.tartaruga.begin_fill()
        for _ in range(4):
            self.tartaruga.forward(self.lado)
            self.tartaruga.right(90)
        self.tartaruga.end_fill()
