import math 

print("Faça um programa que peça um número e apresente na tela o antecessor e o sucessor dele.")

n = int(input("Número: "))
print("Antecessor", n - 1, "Sucessor", n + 1)



print("Faça um programa que peça dois números e imprima a soma deles.")

n1 = int(input("n1: "))
n2 = int(input("n2: "))

print("A soma de n1 com n2 é", n1 + n2)



print("Faça um programa que peça três números e imprima o produto (multiplicação) deles.")

n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

print("A multiplicação de n1 com n2 com n3 é", n1 * n2 * n3)



print("Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética.")

n1 = int(input("Nota 1/4: "))
n2 = int(input("Nota 2/4: "))
n3 = int(input("Nota 3/4: "))
n4 = int(input("Nota 4/4: "))

print("A média aritmética das notas é:", (n1 + n2 + n3 + n4) / 4)



print("Faça um programa que converta metros para centímetros.")

metro = float(input("Valor em metros: "))
print(metro, "m = ", metro * 100, "cm")



print("Faça um programa que peça o raio de um círculo, calcule e mostre sua área.")

raio = float(input("Raio: "))
print("Área = ", 3.14159265 * (raio ** 2))



print("Faça um programa que peça a medida do lado de um quadrado, calcule e mostre sua área. Em seguida, mostre também o perímetro do quadrado para o usuário.")

n1 = int(input("Lado do quadrado: "))

print("Área:", (n1 * n1), "\nPerímetro:", (n1 * 4))



print("Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no dia. Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês (considerando 30 dias).")

ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_por_dia = float(input("Quantas horas você trabalha por dia? "))
ganho_por_dia = ganho_por_hora * horas_por_dia

print("Por dia você ganha", "R$", ganho_por_dia)
print("Por mês você ganha", "R$", ganho_por_dia * 30)



print("Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius")

f = float(input("Valor em °F: "))

print("O valor em °C é:", 5 * (f - 32) / 9)



print("Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²")

altura = float(input("Altura em metros: "))
peso = float(input("Peso em quilos: "))
print("IMC =", peso / (altura ** 2))



print("Dada a equação: ax² + bx + c = 0 peça para o usuário informar o valor de a, b e c e calcule x' e x\"")

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = (b ** 2) - (4 * a * c)
x1 = ((-b) + (delta ** 0.5)) / (2 * a)
x2 = ((-b) - (delta ** 0.5)) / (2 * a)

print("Delta = ", delta)
print("x\' = ", x1)
print("x\" = ", x2)



print("Faça um programa em Python que receba o nome, o desconto (%) e o valor de um produto. Em seguida, apresente um relatório com o nome, o valor atual, o desconto (em reais) e o valor final do produto ")

nome = input("Nome do produto: ")
valor = float(input("Valor do produto: "))
desconto = float(input("Desconto: "))
valorDesconto = valor * (desconto / 100)

valorFinal = valor - valorDesconto 

print("\n")

# ---- Linha --------------
for i in range(32):
    print("-", end="")

# Nome do Produto
print("\nNome do produto:", nome)

# ---- Linha --------------
for i in range(32):
    print("-", end="")

# Valor:
print("\nValor: R$", '%.2f' % valor)

# Desconto:
print("Desconto: R$", '%.2f' % valorDesconto)

# ---- Linha --------------
for i in range(32):
    print("-", end="")

# Valor final:
print("\nValor final: R$", '%.2f' % valorFinal)

# ---- Linha --------------
for i in range(32):
    print("-", end="")



print("Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$450,00. O programa deve informar ao usuário a quantidade de latas de tinta a serem compradas e o preço total.")

areaPintada = float(input("Área a ser pintada em metros quadrados: "))
# 1 lata == 18 L == R$450.00 == 108 m²

lataPreco = 450 
areaPorLitro = 6 # m²

totalLatas = areaPintada 
# voce precisa comprar X latas


"""
x == 
"""



print("Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre um relatório com o valor total do seu salário no referido mês (salário bruto), sabendo-se que são descontados 7.5% para o Imposto de Renda, 8% para o INSS e 1% para o sindicato.")

# Modelo de relatório:
# + Salário Bruto: R$
# - IR (7.5%): R$
# - INSS (8%): R$
# - Sindicato (1%): R$
# = Salário Líquido: R$

