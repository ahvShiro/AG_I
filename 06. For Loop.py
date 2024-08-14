# 1) Faça um programa em Python utilizando o for (um programa pra cada um), que:
# a) Apresente os números de 1 a 100 (um por linha).

# for i in range(1, 101):
#     print(i)


# b) Apresente os números de 100 a 1 (um por linha).

# for i in range(100, 0, -1):
#     print(i)


# c) Apresente os números pares de 1 a 100 (um por linha).

# for i in range(2, 101, 2):
#     print(i)

# OU

# for i in range(1, 101):
#     if(i % 2 == 0):
#         print(i)


# d) Apresente os números ímpares de 1 a 100 (um por linha).

# for i in range(1, 101, 2):
#     print(i)

# OU

# for i in range(1, 101):
#     if(i % 3 == 0):
#         print(i)


# e) Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.

# soma = 0
# for i in range(1, 101):
#     soma += i
# print(soma)


# f) Faça a soma dos números de X a Y (informados pelo usuário), 
# desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).

x = int(input("Valor de X (menor que Y):"))
y = int(input("Valor de Y (maior que X):"))
soma = 0

for i in range(x, y + 1):
    soma += i
print(soma)


# g) Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. 
# Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120

j = int(input("j: "))

# for i in 
