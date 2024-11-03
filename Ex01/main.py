# main.py

import turtle
from circulo import Circulo
from quadrado import Quadrado

def main():
    # Cria a tela
    turtle.bgcolor("white")

    # Desenho de um círculo
    circulo = Circulo(100, "blue")
    circulo.desenhar()

    # Move a tartaruga para uma nova posição
    circulo.limpar()
    circulo.tartaruga.penup()
    circulo.tartaruga.goto(-150, 0)
    circulo.tartaruga.pendown()

    # Desenho de um quadrado
    quadrado = Quadrado(100, "red")
    quadrado.desenhar()

    # Finaliza o desenho
    turtle.done()

if __name__ == "__main__":
    main()
