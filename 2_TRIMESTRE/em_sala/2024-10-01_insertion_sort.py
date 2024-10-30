vetor = [5, 4, 3, 2, 1]

for i in len(1, len(vetor)):

    j = i - 1
    
    while(j >= 0 and vetor[i] < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
    
    vetor[j + 1] = vetor[i]