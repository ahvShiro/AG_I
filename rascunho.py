

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

# preco = 100
# juros = 0.01

juros = float(input("Digite os juros em decimal: "))
valorInicial = float(input("Digite o valor inicial: "))
valorFinal = float(input("Digite o valor final: "))

mes = 0
preco = valorInicial

while (preco <= valorFinal):
    mes += 1
    preco += preco * juros

anos = int(mes / 12)
meses = mes % 12

print(f"{anos} anos e {meses} meses para R${valorInicial:.2f} virarem R${valorFinal:.2f}")



