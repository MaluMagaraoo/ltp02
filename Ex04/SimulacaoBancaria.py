# simulacao_bancaria.py
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca


def menu(conta):
    while True:
        print("\nEscolha uma operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Saldo")
        print("4. Ver Histórico")
        print("5. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
            print("Depósito realizado com sucesso.")

        elif escolha == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso.")

        elif escolha == '3':
            conta.exibir_informacoes()

        elif escolha == '4':
            conta.ver_historico()

        elif escolha == '5':
            print("Saindo do sistema.")
            break

        else:
            print("Escolha inválida. Tente novamente.")


def main():
    cc = ContaCorrente("12345", "João", 1000, 500)
    cp = ContaPoupanca("67890", "Maria", 1500, 0.02)

    while True:
        print("\nEscolha uma conta para operar:")
        print("1. Conta Corrente")
        print("2. Conta Poupança")
        print("3. Sair")

        escolha_conta = input("Digite sua escolha: ")

        if escolha_conta == '1':
            menu(cc)  # Inicia o menu para a conta corrente
        elif escolha_conta == '2':
            menu(cp)  # Inicia o menu para a conta poupança
        elif escolha_conta == '3':
            print("Saindo do sistema.")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()

