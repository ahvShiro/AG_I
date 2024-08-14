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


option = int(input("== Menu de Opções ==\n1. Gerar um número aleatório entre X e Y\n2. X é par ou ímpar?\n3. Valor R$X com Y% de desconto\n4. Calcular X e Y com o operador informado (+, -, * ou /)\n== Opção escolhida: "))

match option:
    case 1:
        x = int(input("x = "))
        y = int(input("y = "))
        print(f"Entre {x} e {y}: {random.randint(x, y)}")
    case 2:
        x = int(input("x = "))
        if (x % 2 == 0):
            print("Par")
        else:
            print("Ímpar")
    case 3:
        x = float(input("x = "))
        y = int(input("y = "))
        result = (x * y) / 100
        print(f"R${x:.2f} com {y}% de desconto = {result}")
    case 4:
        x = float(input("x = "))
        y = float(input("y = "))
        operator = input("operador = ")

        if (operator == "+"):
            result = x + y

        if (operator == "-"):
            result = x - y

        if (operator == "/"):
            result = x / y

        if (operator == "*"):
            result = x * y

        print(f"{x} {operator} {y} = {result}")
    case _:
        print("Opção não existe. Tente novamente")




