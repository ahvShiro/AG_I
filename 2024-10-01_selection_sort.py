# Menor vem pra frente


vetor = [5, 4, 3, 2, 1]

for i in range(0, len(vetor) - 1):

    # Achar o índice do menor valor
    menor = i

    # Itera pela area de busca do vetor
    for j in range(i + 1, len(vetor)):
        # Se o cursor for menor que o menor numero até agora:
        if(vetor[j] < vetor[menor]):
            # Guarda o cursor como o menor
            menor = j
    
    # Troca
    x = vetor[i]
    vetor[i] = vetor[menor]
    vetor[menor] = x

print(vetor)