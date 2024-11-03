# pneu.py

class Pneu:
    def __init__(self, tipo):
        self.tipo = tipo

    def status(self):
        return f"Pneu do tipo {self.tipo}."
