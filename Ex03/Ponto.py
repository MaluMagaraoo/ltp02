import turtle


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"


def mover_para_ponto(ponto):
    turtle.penup()
    turtle.goto(ponto.x, ponto.y)
    turtle.pendown()  #


turtle.title("Movendo a Turtle com Ponto")
turtle.speed(1)


ponto1 = Ponto(100, 150)
ponto2 = Ponto(-150, -100)


mover_para_ponto(ponto1)
turtle.dot(10, "red")
mover_para_ponto(ponto2)
turtle.dot(10, "blue")


turtle.done()
