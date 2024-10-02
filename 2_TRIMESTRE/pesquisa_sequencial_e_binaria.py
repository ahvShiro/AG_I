print("===== Busca Sequencial =====")

size = int(input("tamanho: "))

array = [0] * size

for i in range(0, size):
    array[i] = int(input(f"posição {i}: "))

query = int(input("busca: "))

for i in range(0, len(array)):
    if(array[i] == query):
        print(f"O valor {array[i]} está na posição {i}")
        break

else:
    print("Valor não encontrado")



print("===== Busca Binária =====")

size = int(input("tamanho: "))
array = [0] * size

print("Insira os itens em ordem")
for i in range(0, size):
    array[i] = int(input(f"posição {i}: "))


valor = int(input("Valor a ser pesquisado: "))
posicao_do_valor = -1

esquerda = 0
direita = len(array) - 1

while esquerda <= direita:

    meio = (esquerda + direita) // 2

    if(valor == array[meio]):
        posicao_do_valor = meio
        break
    elif(valor > array[meio]):
        esquerda = meio + 1
    else:
        direita = meio - 1

if(posicao_do_valor != -1):
    print(f"{valor} está na posição {posicao_do_valor}")
else:
    print(f"{valor} não existe no vetor")

