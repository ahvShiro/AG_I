# === BIBLIOTECAS =========================================

#   Conjunto de código criado para determinado fim
#   Importada no começo do algoritmo


# === random ==============================================

import random

#   A biblioteca random gera números aleatórios
#   Uso de funções: nome_da_biblioteca.nome_da_funcao()
#   Cada função tem um parâmetro

d20 = random.randint(1, 20)
# Retorna um int n sendo arg1 <= n <= arg2


# === EXERCÍCIO 1 =========================================

numeroAleatorio = random.randint(10, 20)
print("sorteou " + str(numeroAleatorio) + "\n" + str(numeroAleatorio - 1) + ", " + str(numeroAleatorio) + " e " + str(numeroAleatorio + 1))
# sorteou 14
# 13, 14 e 15


# === EXERCÍCIO 2 =========================================

n1 = int(input("n1: "))
n2 = int(input("n2: "))

if n1 > n2:
    temp = n1
    n1 = n2
    n2 = temp

aleatorioIntervalo = random.randint(n1, n2)
print("Número aleatório nesse intervalo:", aleatorioIntervalo)


# === math ================================================

import math


