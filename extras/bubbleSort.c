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

void selectionSort(int vetor[], int tamanho) {
    for(int i = 0; i < tamanho - 1; i++) {
        int menor = i;
        for(int j = i + 1; j < tamanho; j++ ) {
            if(vetor[j] < vetor[menor]) {
                menor = j;
            }
        }
        int x = vetor[menor];
        vetor[menor] = vetor[i];
        vetor[i] = x;
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

    printVetor(vetor, tamanhoVetor);

    selectionSort(vetor, tamanhoVetor);

    printVetor(vetor, tamanhoVetor);
}