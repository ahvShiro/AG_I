
# %% Bubble Sort
vetor = [5, 4, 3, 2, 1]

for i in range(0, len(vetor) - 1):
    for j in range(0, len(vetor) - 1):
        if(vetor[j] > vetor[j + 1]):
            x = vetor[j]
            vetor[j] = vetor[j + 1]
            vetor[j + 1] = x
        break

print(vetor)

# %% Selection Sort
vetor = [5, 4, 3, 2, 1]

for i in range(0, len(vetor) - 1):
    menor = i
    for j in range(menor + 1, len(vetor)):
        if(vetor[j] < vetor[menor]):
            x = vetor[menor]
            vetor[menor] = vetor[j]
            vetor[j] = x

print(vetor)


# %% Insertion Sort
vetor = [5, 4, 3, 2, 1]

for i in range(1, len(vetor)):

    anterior = i - 1
    atual = vetor[i]

    while(anterior >= 0 and atual < vetor[anterior]):
        vetor[anterior + 1] = vetor[anterior]
        anterior -= 1

    vetor[anterior + 1] = atual

print(vetor)


