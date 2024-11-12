#include <stdio.h>

void bubbleSort(int vetor[], int tamanho) {    
    for(int i = 0; i < tamanho - 1; i++) {
        for(int j = 0; j < tamanho - 1 - i; j++) {
            if(vetor[j] > vetor[j + 1]) {
                int x = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = x;
            }
        }
    }
}

void printVetor(int vetor[], int tamanho) {
    printf("[");
    for(int i = 0; i < tamanho; i++) {
        printf("%d", vetor[i]);
        if (i < tamanho - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}


int main() {
    int tamanhoVetor = 0;

    printf("Tamanho do vetor: ");
    scanf("%d", &tamanhoVetor);

    int vetor[tamanhoVetor];
    for(int i = 0; i < tamanhoVetor; i++) {
        printf("vetor[%i]: ", i);
        scanf("%d", &vetor[i]);
    }

    bubbleSort(vetor, tamanhoVetor);

    printVetor(vetor, tamanhoVetor);
}