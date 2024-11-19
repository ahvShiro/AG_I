import random as r

def imprimirVetor(vetor: list) -> list:
    print("[", end='')

    for i in range(0, len(vetor)):
        if(i < (len(vetor) - 1)):
            print(f"{vetor[i]}", end=', ')

        elif(i == (len(vetor) - 1)):
            print(f"{vetor[i]}]")


def gerarVetor(tam_vetor: int, tipo_dado: str) -> list:

    tipo_dado.lower()

    if(tipo_dado == "int"):
        vetor = [0] * tam_vetor
        for i in range(0, len(vetor)):
            vetor[i] = r.randint(1, 100)
        return vetor

    elif(tipo_dado == "float"):
        vetor = [0.0] * tam_vetor
        for i in range(0, len(vetor)):
            vetor[i] = r.uniform(1, 100)
        return vetor

    else:
        vetor = []
        return vetor


def ordenaBolha(vetor: list) -> list:
    for i in range(0, len(vetor) - 1):
        for j in range(0, len(vetor) - 1):
            if vetor[j] > vetor[j + 1]:
                x = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = x




def main():
    vetor = gerarVetor(5, "int")

    imprimirVetor(vetor)

    ordenaBolha(vetor)

    imprimirVetor(vetor)





if(__name__ == "__main__"):
    main()