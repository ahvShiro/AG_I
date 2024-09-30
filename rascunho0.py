# import random

# par = 0
# impar = 0
# multiplo_de_tres = 0
# soma_total = 0
# media = 0
# iteracoes_validas = 0

# for i in range(30):
#     num = random.randint(0, 100)

#     # CONDIÇÕES QUE IGNORAM ITERAÇÕES
#     if(num == 50):
#         break
#     if(num % 5 == 0):
#         continue

#     # CONDIÇÕES PARA SEREM IMPRESSAS
#     if(num % 2 == 0):
#         par += 1
#     else:
#         impar += 1
#     if (num % 3 == 0):
#         multiplo_de_tres += 1

#     # SOMA DE VARIÁVEIS A CADA ITERAÇÃO
#     soma_total += num
#     iteracoes_validas += 1

# media = round((soma_total / iteracoes_validas), 2)

# print(f"Quantidade de pares: {par}")
# print(f"Quantidade de ímpares: {impar}")
# print(f"Múltiplos de 3: {multiplo_de_tres}")
# print(f"Soma de todos: {soma_total}")
# print(f"Média: {media}")






# Python3 code to implement iterative Binary
# Search.


# It returns location of valor in given array arr
def binarySearch(arr, inicial, final, valor):

    while inicial <= final:

        meio = inicial + (final - inicial) // 2

        # Check if valor is present at meio
        if arr[meio] == valor:
            return meio

        # If valor is greater, ignore left half
        elif arr[meio] < valor:
            inicial = meio + 1

        # If valor is smaller, ignore right half
        else:
            final = meio - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    valor = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, valor)
    if result != -1:
        print("Element is present at indevalor", result)
    else:
        print("Element is not present in array")


# Começa no segundo elemento: O primeiro elemento é considerado já ordenado. O algoritmo começa no segundo elemento e o compara com o primeiro.
# Compara e move: Ele verifica se o segundo elemento deve ser inserido antes ou depois do primeiro. 
#   Se for menor, move o primeiro elemento para a direita e insere o segundo elemento na primeira posição.
# Repete para os próvalorimos elementos: Para cada elemento subsequente, ele o compara com os elementos à esquerda (que já estão ordenados) e o insere na posição correta.
# Processo contínuo: Repete isso até que todos os elementos estejam na posição correta.
