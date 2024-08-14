
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