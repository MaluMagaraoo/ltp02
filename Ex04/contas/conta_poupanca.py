# conta_poupanca.py
from .conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial, taxa_juros):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            return True
        else:
            print("Saque negado! Saldo insuficiente.")
            return False

    def calcular_saldo(self):
        self.saldo += self.saldo * self.taxa_juros
