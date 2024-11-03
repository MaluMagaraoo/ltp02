# veiculo.py

from Motor import Motor
from Pneu import Pneu

class Veiculo(Motor, Pneu):
    def __init__(self, potencia, tipo):
        Motor.__init__(self, potencia)  # Inicializa a classe Motor
        Pneu.__init__(self, tipo)        # Inicializa a classe Pneu

    def status(self):
        motor_status = Motor.status(self)  # Chama o status da classe Motor
        pneu_status = Pneu.status(self)    # Chama o status da classe Pneu
        return f"{motor_status}\n{pneu_status}"  # Retorna o status combinado
