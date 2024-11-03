# main.py

from Veiculo import Veiculo

def main():
    # Criação de um veículo com motor de 150 HP e pneu do tipo "radial"
    meu_veiculo = Veiculo(150, "radial")

    # Exibindo o status do veículo
    print(meu_veiculo.status())

if __name__ == "__main__":
    main()
