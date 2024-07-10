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

def promptPaycheck(paycheck_before, percentual, increase, paycheck_after):
    print(f"Salário antes do reajuste: {paycheck_before} \nPercentual de aumento aplicado: {percentual} \nValor do aumento: {increase} \nSalário após aumento: {paycheck_after}")

paycheck = float(input("Salário do colaborador: "))

if (paycheck >= 710):
    percentual = 20
    increase = (paycheck * percentual) / 100
    paycheck_after = paycheck + increase
    promptPaycheck(paycheck, percentual, increase, paycheck_after)

elif (paycheck >= 1000):
    percentual = 15
    increase = (paycheck * percentual) / 100
    paycheck_after = paycheck + increase
    promptPaycheck(paycheck, percentual, increase, paycheck_after)

elif (paycheck >= 2500):
    percentual = 10
    increase = (paycheck * percentual) / 100
    paycheck_after = paycheck + increase
    promptPaycheck(paycheck, percentual, increase, paycheck_after)
else:
    percentual = 5
    increase = (paycheck * percentual) / 100
    paycheck_after = paycheck + increase
    promptPaycheck(paycheck, percentual, increase, paycheck_after)


