from abc import ABC, abstractmethod

# Classe abstrata ContaBancaria
class ContaBancaria(ABC):
    def __init__(self, numero_conta, titular, saldo_inicial):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []

    def registrar_transacao(self, tipo, valor):
        self.historico.append((tipo, valor, self.saldo))

    def exibir_informacoes(self):
        print(f"Conta: {self.numero_conta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo:.2f}")

    def ver_historico(self):
        print(f"Histórico de transações da conta {self.numero_conta}:")
        for tipo, valor, saldo in self.historico:
            print(f"{tipo}: R${valor:.2f}, Saldo após transação: R${saldo:.2f}")

