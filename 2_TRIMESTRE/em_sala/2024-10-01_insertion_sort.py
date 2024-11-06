vetor = [5, 4, 3, 2, 1]

for i in range(1, len(vetor)):

    j = i - 1
    
    while(j >= 0 and vetor[j] > vetor[i]):
        vetor[j + 1] = vetor[j]
        j -= 1
    
    vetor[j + 1] = vetor[i]