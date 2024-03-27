import math

# print("01. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.")

# x = int(input("n: "))

# if(x > 0):
#     print("Positivo")
# else:
#     print("Negativo")



# print("02. Faça um programa que peça dois números e imprima na tela somente o maior deles.")

# x = int(input("x: "))
# y = int(input("y: "))

# if(x > y):
#     m = x
# else:
#     m = y

# print(m, "é MAIOR")



# print("03. Faça um programa que peça a idade do usuário. Se ele for maior de idade, apresente a mensagem “Entrada permitida”. Se não, apresente “Entrada negada”.")

# idade = int(input("Idade: "))

# if(idade >= 18):
#     print("Entrada permitida")
# else:
#     print("Entrada negada")



# print("04. Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.")

# trabalho = int(input("Nota do trabalho: "))
# prova = int(input("Nota da prova: "))

# if(trabalho + prova / 2 >= 60):
#     print("Aprovado")
# else:
#     print("Reprovado")



# print("05. Faça um programa que peça ao aluno o conceito dele na disciplina (A, B, C ou D). Se o conceito for A, B ou C apresente “Aprovado”, se não, apresente “Reprovado”.")

# conceito = input("Conceito: ")

# if(conceito == 'D'):
#     print("Reprovado")
# else:
#     print("Aprovado")



# print("06. Faça um programa que recebe o salário do usuário. Se o usuário recebe menos que um salário mínimo, apresente na tela uma mensagem informando isso a ele. Se o salário dele for maior que o salário mínimo, calcule quantos salários mínimos ele ganha e informe na tela. Considere o valor de R$1.212,00 para o salário mínimo neste exercício")

# salario = float(input("Salário: "))

# if(salario >= 1212):
#     print("Você ganha", (salario / 1212.0), "salários mínimos")
# else:
#     print("Você ganha menos de 1 salário mínimo")



# print("07. Faça um programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada")

# sexo = input("Sexo: ")
# if(sexo.upper() == 'F'):
#     print("Feminino")
# if(sexo.upper() == 'M'):
#     print("Masculino")

# print("Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça para ele digitar o nome dele e informe a mensagem “Bem vindo Fulano”. Caso contrário, apresente “Entrada não permitida”.")

# idade = int(input("Idade: "))

# if(idade < 18):
#     print("Entrada não permitida")
# else:
#     nome = input("Nome: ")
#     print("Bem vindo,", nome)


print("08. Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça o salário dele e dê um aumento de 5%, apresentando na tela o valor final do salário. Se ele for menor, informe a mensagem “Cálculo não permitido”.")

idade = int(input("Idade: "))

if(idade < 18):
    print("Cálculo não permitido")
else:
    salario = float(input("Salário: "))
    print("Salário com 5% de aumento: R$", "{:.2f}".format(salario + (salario * 0.05) ))



print("00. ")