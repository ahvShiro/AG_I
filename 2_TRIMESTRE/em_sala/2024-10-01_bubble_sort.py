vetor = [4, 2, 3, 1, 5]

print(vetor)

# Para cada ciclo
for i in range(0, len(vetor) - 1):
    # Para cada iteração
    for j in range(0, len(vetor) - 1):
        # Se o primeiro for maior do que o segundo
        if(vetor[j] > vetor[j + 1]):
            # Troca
            x = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = x

print(vetor)
