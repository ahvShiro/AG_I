import random

vetor = [0] * 250

for i in range(len(vetor)):
    vetor[i] = i

foiEncontrado = False
valor = int(input("Página a ser buscada: "))
inicio = 0
fim = len(vetor) - 1

while(inicio <= fim):
    meio = random.randint(inicio, fim)
    print(f"Aberto na página {meio}")

    if(valor == vetor[meio]):
        foiEncontrado = True
        break

    elif(valor >= meio and valor <= meio + 10):
        print(f"Procurando as 10 paginas da frente...")
        for i in range(meio, meio + 11, 2):

            print("Procurando de 2 em 2...")
            if(i < len(vetor)):

                if(valor == vetor[i]):
                    foiEncontrado = True
                    break

                if(i - 1 >= 0 and valor == vetor[i - 1]):
                    print(f"Verificando a página anterior {i - 1}")
                    foiEncontrado = True
                    break
        break

    if(valor <= meio and valor >= meio - 10):
        print(f"Procurando as 10 paginas da frente...")
        for i in range(meio, meio - 11, -2):

            print("Procurando de 2 em 2...")
            if(i < len(vetor)):
                
                if(valor == vetor[i]):
                    foiEncontrado = True
                    break
            
                if(i - 1 >= 0 and valor == vetor[i - 1]):
                    print(f"Verificando a página anterior...")
                    foiEncontrado = True
                    break

        break


    elif(valor > vetor[meio]):
        inicio = meio + 1
        print("Procurando depois...")

    else:
        fim = meio - 1
        print("Procurando antes...")

if(foiEncontrado):
    print(f"Página {valor} foi encontrada")
else:
    print(f"Página não existe")






