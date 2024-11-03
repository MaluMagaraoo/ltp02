# motor.py

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def status(self):
        return f"Motor com potência de {self.potencia} HP."
