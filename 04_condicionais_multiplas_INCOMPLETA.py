import random


# 1) Construa um programa que mostre menu exatamente como o exemplo abaixo e implemente o código necessário para seu funcionamento:

# menu_string = "== Menu de Opções == \n1. Somar X e Y \n2. Potência Y de um número X (x^y) \n3. Raiz quadrada de X \n4. Gerar um número aleatório \n== Opção escolhida: "
# option = int(input(menu_string))
# match option:
#     case 1:
#         x = float(input("x: "))
#         y = float(input("+ y: "))
#         print(f"{x} + {y} = {x + y}")
#     case 2:
#         x = float(input("x: "))
#         y = float(input("^ y: "))
#         print(f"{x} ^ {y} = {x ** y}")
#     case 3:
#         x = float(input("x: "))
#         print(f"Raíz quadrada de {x} = {x ** (1/2)}")
#     case 4:
#         x = int(input("Mínimo: "))
#         y = int(input("Máximo: "))
#         print(f"Número aleatório entre {x} e {y}: {random.randint(x, y)}")
#     case _:
#         print("Opção não identificada. Tente novamente")


# menu_string = "== Menu de Opções == \n1. Somar X e Y \n2. Potência Y de um número X (x^y) \n3. Raiz quadrada de X \n4. Gerar um número aleatório \n== Opção escolhida: "
# option = int(input(menu_string))

# if (option == 1):
#     x = float(input("x: "))
#     y = float(input("+ y: "))
#     print(f"{x} + {y} = {x + y}")
# elif (option == 2):
#     x = float(input("x: "))
#     y = float(input("^ y: "))
#     print(f"{x} ^ {y} = {x ** y}")
# elif (option == 3):
#     x = float(input("x: "))
#     print(f"Raíz quadrada de {x} = {x ** (1/2)}")
# elif (option == 4):
#     x = int(input("Mínimo: "))
#     y = int(input("Máximo: "))
#     print(f"Número aleatório entre {x} e {y}: {random.randint(x, y)}")
# else:
#     print("Opção não identificada. Tente novamente")


# 2) Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corporal), que é definida como sendo a relação entre o peso e o quadrado da altura (informada em metros, ex: 1.80) do indivíduo. Ou seja: IMC = peso/altura² e a situação do peso é determinada pela tabela abaixo:

# resultados menores que 16 — magreza grave;
# resultados entre 16 e 16,9 — magreza moderada;
# resultados entre 17 e 18,5 — magreza leve;
# resultados entre 18,6 e 24,9 — peso ideal;
# resultados entre 25 e 29,9 — sobrepeso;
# resultados entre 30 e 34,9 — obesidade grau I;
# resultados entre 35 e 39,9 — obesidade grau II ou severa;
# resultados maiores do que 40 — obesidade grau III ou mórbida

# peso = float(input("Insira seu peso em Kg: "))
# altura = float(input("Insira sua altura em metros: "))

# imc = (peso / (altura * altura))

# if (imc < 16):
#     print("magreza grave")
# elif (imc <= 16.9):
#     print("magreza moderada")
# elif (imc <= 18.5):
#     print("magreza leve")
# elif (imc <= 24.9):
#     print("peso ideal")
# elif (imc <= 29.9):
#     print("sobrepeso")
# elif (imc <= 34.9):
#     print("obesidade grau I")
# elif (imc <= 39.9):
#     print("obesidade grau II ou severa")
# else:
#     print("obesidade grau III ou mórbida")

# 3) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e o contrataram para desenvolver 
# o programa que vai calcular os reajustes. Faça um programa que recebe o salário de um colaborador e calcule o reajuste 
# segundo o seguinte critério baseado no salário atual:

# até R$ 710,00 (incluindo): aumento de 20%
# entre R$ 710,00 e R$ 1.000,00: aumento de 15%
# entre R$ 1.000,00 e R$ 2.500,00: aumento de 10%
# de R$ 2.500,00 em diante: aumento de 5% 

# Após o aumento ser realizado, informe na tela:
# - salário antes do reajuste;
# - percentual de aumento aplicado;
# - valor do aumento;
# - novo salário, após o aumento.


# paycheck = float(input("Salário do colaborador: "))

# if (paycheck <= 710):
#     percentual = 20

# elif (paycheck <= 1000):
#     percentual = 15

# elif (paycheck <= 2500):
#     percentual = 10

# else:
#     percentual = 5

# paycheck_before = paycheck
# increase = (paycheck * percentual) / 100
# paycheck_after = paycheck + increase
# print(f"Salário antes do reajuste: R${paycheck_before:.2f} \nPercentual de aumento aplicado: {percentual}% \nValor do aumento: R${increase:.2f} \nSalário após aumento: R${paycheck_after:.2f}")

# 4) Crie um algoritmo que receba o valor de x, calcule e imprima o valor de f(x):


# x = float(input("x = "))
# if (x <= 1):
#     print("f(x) = 1")
# elif (x <= 2):
#     print("f(x) = 2")
# elif (x <= 3):
#     print(f"f(x) = {x ** 2}")
# else:
#     print(f"f(x) = {x ** 3}")

# 5) == Menu de Opções ==
# 1. Gerar um número aleatório entre X e Y
# 2. X é par ou ímpar?
# 3. Valor R$X com Y% de desconto
# 4. Calcular X e Y com o operador informado (+, -, * ou /)
# == Opção escolhida:


# option = int(input("== Menu de Opções ==\n1. Gerar um número aleatório entre X e Y\n2. X é par ou ímpar?\n3. Valor R$X com Y% de desconto\n4. Calcular X e Y com o operador informado (+, -, * ou /)\n== Opção escolhida: "))

# match option:
#     case 1:
#         x = int(input("x = "))
#         y = int(input("y = "))
#         print(f"Entre {x} e {y}: {random.randint(x, y)}")
#     case 2:
#         x = int(input("x = "))
#         if (x % 2 == 0):
#             print("Par")
#         else:
#             print("Ímpar")
#     case 3:
#         x = float(input("x = "))
#         y = int(input("y = "))
#         result = (x * y) / 100
#         print(f"R${x:.2f} com {y}% de desconto = {result}")
#     case 4:
#         x = float(input("x = "))
#         y = float(input("y = "))
#         operator = input("operador = ")

#         if (operator == "+"):
#             result = x + y

#         if (operator == "-"):
#             result = x - y

#         if (operator == "/"):
#             result = x / y

#         if (operator == "*"):
#             result = x * y

#         print(f"{x} {operator} {y} = {result}")
#     case _:
#         print("Opção não existe. Tente novamente")




# 6) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:


# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

# print("Responda \"1\" para sim e \"0\" para não")

# a = int(input("Telefonou para a vítima? "))
# b = int(input("Esteve no local do crime? "))
# c = int(input("Mora perto da vítima? "))
# d = int(input("Devia para a vítima? "))
# e = int(input("Já trabalhou com a vítima? "))

# total = a + b + c + d + e

# if(total == 0):
#     print("Inocente")
# elif(total <= 2):
#     print("Suspeita")
# elif(total <= 4):
#     print("Cúmplice")
# elif(total == 5):
#     print("Assasino")


# 7) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver 
# o programa que calcula os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
# critério, baseado no salário atual:

# salários até R$ 2.800,00 (incluindo) : aumento de 20%
# salários entre R$ 2.800,00 e R$ 7.000,00 : aumento de 15%
# salários entre R$ 7.000,00 e R$ 15.000,00 : aumento de 10%
# salários de R$ 15.000,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salario = float(input("Salário: "))
percentual = 0

if(salario <= 2800):
    percentual = 20
elif(salario <= 7000):
    percentual = 15
elif(salario <= 15000):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
salario_depois = aumento + salario

print(f"Salário antes: {salario}")
print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: {aumento}")
print(f"Salário depois: {salario_depois}")



# 8) Crie um algoritmo que leia o número do mês (1 a 12) e emita na tela uma mensagem informando o nome do mês e a quantidade
# de dias que ele possui.





# 9) Crie um programa que simula o funcionamento de uma calculadora, ou seja, emita o resultado da operação entre dois operandos
# a partir da leitura dos mesmos e do operador. Considere que os possíveis operadores são: (+) adição, (-) subtração, 
# (x) multiplicação e (/) divisão.






# 10) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 5,49 o preço do litro do álcool é R$ 3,59.


# 11) Uma frutaria está vendendo frutas com a seguinte tabela de preços:

# Até 5 Kg
# Acima de 5 Kg
# Morango
# R$ 18,90 por Kg
# R$ 17,50 por Kg
# Maçã
# R$ 9,50 por Kg
# R$ 7,90 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$50,00, receberá ainda um desconto de 5% sobre este 
# total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos, a quantidade (em Kg) de maçãs adquiridas e calcule o valor a ser
# pago pelo cliente.


# 12) Faça um programa para calcular a quantidade de notas de um troco. O programa deverá perguntar ao usuário o valor do troco (inteiro) 
# e depois informar quantas notas (considere R$1 como nota, pois temos moeda) de cada valor serão fornecidas. As notas disponíveis 
# serão as de 1, 2, 5, 10, 20, 50 e 100 reais.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, duas notas de 20, uma nota de 5 e duas de 2.
# Dica: utilize funções da biblioteca math (teto e chão, por exemplo), o resto da divisão ou a parte inteira da divisão para realizar os cálculos. NÃO utilize laço de repetição.
