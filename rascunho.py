

# # for i in range(altura):
# #     # # SPACING
# #     # for spacing in range(altura - j - 1):
# #     #     print(" ", end="")
# #     # # ROW
# #     for j in range(i + 1):
# #         print("#", end="")
# #     # LINE BREAK
# #     print()


# altura = int(input("altura: "))

# i = 0
# while i < altura:
#     j = 0
#     while j <= i:
#         print("#", end='')
#         j += 1
#     print()
#     i += 1


# 30/07/2024 AG_I #######################################################

# # preco = 100
# # juros = 0.01

# juros = float(input("Digite os juros em decimal: "))
# valorInicial = float(input("Digite o valor inicial: "))
# valorFinal = float(input("Digite o valor final: "))

# mes = 0
# preco = valorInicial

# while (preco <= valorFinal):
#     mes += 1
#     preco += preco * juros

# anos = int(mes / 12)
# meses = mes % 12

# print(f"{anos} anos e {meses} meses para R${valorInicial:.2f} virarem R${valorFinal:.2f}")


# 13/08/2024 

import random

even_nums = 0
odd_nums = 0
multiple_of_three = 0
total_sum = 0
average = 0

for i in range(30):
    num = random.randint(0, 100)

    if(num % 2 == 0):
        even_nums += 1
    else:
        odd_nums += 1

    if(num % 3 == 0):
        multiple_of_three += 1

    total_sum += num

average = round((total_sum / 30), 2)

print(f"Quantidade de pares: {even_nums}")
print(f"Quantidade de ímpares: {odd_nums}")
print(f"Múltiplos de 3: {multiple_of_three}")
print(f"Soma de todos: {total_sum}")
print(f"Média: {average}")


