# conta_corrente.py
from .conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial, limite_cheque_especial):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite_cheque_especial:
            self.saldo -= valor
            return True
        else:
            print("Saque negado! Limite de cheque especial excedido.")
            return False

    def calcular_saldo(self):
        # Na conta corrente, não há cálculo de juros
        pass

