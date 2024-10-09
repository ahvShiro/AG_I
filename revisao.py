# # Bubble sort
# vetor = [3, 2, 5, 4, 1]
# print(vetor)

# # Itera um ciclo
# for i in range(0, len(vetor) - 1):
#     # Itera dentro do vetor
#     for j in range(0, len(vetor) - 1):
#         # Se o primeiro for maior que o segundo
#         if(vetor[j] > vetor[j + 1]):
#             # Troca
#             x = vetor[j]
#             vetor[j] = vetor[j + 1]
#             vetor[j + 1] = x

# print(vetor)


# # Selection Sort
# vetor = [3, 2, 5, 4, 1]
# print(vetor)





# # Insertion Sort
# vetor = [3, 2, 5, 4, 1]
# print(vetor)






# # Busca Sequêncial
# vetor = [3, 2, 5, 4, 1]
# vetor.sort()
# print(vetor)

# valor = int(input("Valor a ser buscado: "))
# foiEncontrado = False

# for i in range(0, len(vetor)):
#     if(valor == vetor[i]):
#         foiEncontrado = True
#         break
#     elif(valor < vetor[i]):
#         break

# if(foiEncontrado):
#     print(f"Valor {valor} encontrado")
# else:
#     print(f"Valor {valor} não encontrado")




# Busca Binária
vetor = [3, 2, 5, 4, 1]
vetor.sort()
print(vetor)

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





