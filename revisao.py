def bubbleSort(vetor):
    # Itera um ciclo
    for i in range(0, len(vetor) - 1):
        print(f"== Ciclo {i+1} =======")

        # Itera dentro do vetor
        for j in range(0, len(vetor) - 1 - i):
            print(vetor)

            # Se o primeiro for maior que o segundo
            if(vetor[j] > vetor[j + 1]):
                print(f"Trocando {vetor[j]} com {vetor[j + 1]}")

                # Troca
                x = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = x

    return(vetor)

def selectionSort(vetor):
    # Itera um ciclo
    for i in range(0, len(vetor)):
        print(f"== Ciclo {i + 1} =======")
        print(f"Estado atual do vetor: {vetor}")

        # Define o indice do menor valor encontrado até agr
        indiceMenorValor = i

        # Descobre o indice do menor valor no vetor
        for j in range(i + 1, len(vetor)):
            print(f"Comparando {vetor[j]} com {vetor[indiceMenorValor]}")
            if vetor[j] < vetor[indiceMenorValor]:
                indiceMenorValor = j

        # Imprime o indice do menor valor encontrado
        print(f"Menor valor encontrado: {vetor[indiceMenorValor]} na posição [{indiceMenorValor}]")

        # Confere se o elemento atual não é o menor
        if(i != indiceMenorValor):
            
            # Troca
            print(f"Trocando {vetor[i]} com {vetor[indiceMenorValor]}")
            x = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = x
        
    return vetor


def insertionSort(vetor):
    return(vetor)



tam = int(input("== Insira o tamanho do vetor ==\n"))
vetor = [0] * tam
for i in range(0, len(vetor)):
    vetor[i] = int(input(f"Valor da posição [{i}]: "))



ans = int(input("== Selecione um algoritmo ==\n1. Bubble Sort 🫧\n2. Selection Sort ⤵️\n3. Insertion Sort 🃏\n"))

match ans:
    case 1:
        bubbleSort(vetor)
    case 2:
        selectionSort(vetor)
    case 3:
        insertionSort(vetor)
    case _:
        print("Digite um valor válido")


print(f"Vetor ordenado: {vetor}")




exit()

# Busca Sequêncial
vetor = [3, 2, 5, 4, 1]
vetor.sort()
print(vetor)

valor = int(input("Valor a ser buscado: "))
foiEncontrado = False

for i in range(0, len(vetor)):
    if(valor == vetor[i]):
        foiEncontrado = True
        break
    elif(valor < vetor[i]):
        break

if(foiEncontrado):
    print(f"Valor {valor} encontrado")
else:
    print(f"Valor {valor} não encontrado")




# Busca Binária
foiEncontrado = False
valor = int(input("Valor a ser buscado: "))
inicio = 0
fim = len(vetor) - 0

while(fim <= inicio):
    meio = (inicio + fim) // 2
    if(valor == vetor[meio]):
        foiEncontrado = True
        break
    elif(valor > vetor[meio]):
        inicio = meio + 1
    else:
        fim = meio + 1

if(foiEncontrado):
    print(f"Valor {valor} foi encontrado")
else:
    print(f"Valor {valor} não encontrado")





