
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
        if(vetor[menor] > vetor[j]):
            x = vetor[menor]
            vetor[menor] = vetor[j]
            vetor[j] = x

print(vetor)


# %% Insertion Sort >-<
vetor = [5, 4, 3, 2, 1]

for i in range(1, len(vetor)):

    indx_anterior = i - 1
    val_atual = vetor[i]

    while(indx_anterior >= 0 and val_atual < vetor[indx_anterior]):
        vetor[indx_anterior + 1] = vetor[indx_anterior]
        indx_anterior -= 1

    vetor[indx_anterior + 1] = val_atual

print(vetor)


