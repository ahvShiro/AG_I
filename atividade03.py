import math
import random

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



# print("08. Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça para ele digitar o nome dele e informe a mensagem “Bem vindo Fulano”. Caso contrário, apresente “Entrada não permitida”.")

# idade = int(input("Idade: "))

# if(idade < 18):
#     print("Entrada não permitida")
# else:
#     nome = input("Nome: ")
#     print("Bem vindo,", nome)



# print("09. Faça um programa que peça a idade do usuário. Se ele for maior de idade, peça o salário dele e dê um aumento de 5%, apresentando na tela o valor final do salário. Se ele for menor, informe a mensagem “Cálculo não permitido”.")

# idade = int(input("Idade: "))

# if(idade < 18):
#     print("Cálculo não permitido")
# else:
#     salario = float(input("Salário: "))
#     print("Salário com 5% de aumento: R$", "{:.2f}".format(salario + (salario * (5 / 100)) ))



# print("10. Faça um programa que peça um número inteiro ao usuário. Se ele for maior do que zero e menor que 100, apresente a mensagem “Número no intervalo definido”, se não, apresente “Número fora do intervalo!”")

# i = int(input("int: "))

# if(0 < i < 100):
#     print("Número fora do intervalo!")
# else:
#     print("Número no intervalo definido")



# print("11. Faça um programa que peça um valor e informe na tela se o número é par ou ímpar.")

# par_ou_impar = int(input("Valor: "))

# if(par_ou_impar % 2 == 0):
#     print("Par")
# else:
#     print("Ímpar")



# print("12. Faça um programa que peça um número e informe se este número é múltiplo de 3.")

# multiplo_tres = int(input("Valor: "))

# if(multiplo_tres % 3 == 0):
#     print("Esse valor é múltiplo de 3")
# else:
#     print("Esse valor não é múltiplo de 3")



# print("13. Faça um programa que gera um número aleatório entre 1 e 10. Em seguida, peça para o usuário digitar um número. Se ele acertar, apresente na tela “Acertou”, se não, “Errou”.")

# numero_para_adivinhar = random.randint(1, 10)

# resposta = int(input("Adivinhe um número de 1 a 10: "))

# if(numero_para_adivinhar == resposta):
#     print("Acertou")
# else:
#     print("Errou")



# print("14. Faça um programa que gera um número aleatório entre X e Y. Para isso, peça para o usuário um valor para X, Y e um número entre X e Y. Gere um valor aleatório entre X e Y e verifique se ele é igual ao número digitado pelo usuário. Se ele acertar, apresente na tela “Acertou”, se não, “Errou”.")

# x = int(input("x: "))
# y = int(input("y: "))

# resposta = int(input("Digite um número nesse intervalo: "))

# if(random.randint(x, y) == resposta):
#     print("Acertou")
# else:
#     print("Errou")



# print("15. Faça um programa que leia três valores: A, B, C. Em seguida, verifique se a soma de A + B é maior que C. Se for, apresente “A+B é maior que C”. Se não, apresente “C é maior que todos!”.")

# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))

# if(a + b > c):
#     print("A+B é maior que C")
# else:
#     print("C é maior que todos!")



# print("16. Faça um algoritmo que peça um número inteiro para o usuário. Se esse número for par, some ele + 5, se não, multiplique o número por 2.")

# numero = int(input("Numero: "))

# if(numero % 2 == 0):
#     numero = numero + 5
# else:
#     numero = numero * 2



# print("17. Faça um programa que peça para o usuário digitar um número inteiro. Se esse número for negativo, peça para ele digitar um número novamente. Por fim, independente do valor, multiplique o número por 10 e informe o resultado na tela")

# i = int(input("Numero: "))

# while(i < 0):
# 	print("Digite novamente")
# 	i = int(input("Numero: "))

# print(i * 10)



print("18. Faça um programa para pedir um número inteiro. Se esse número for positivo, verifique e informe se ele é par ou ímpar. Se ele for negativo, some 100 e apresente na tela.")

numero = int(input("Numero: "))

if(numero > 0):
    if(numero % 2 == 0):
        print("Par")
    else:
        print("Ímpar")
else:
    print(numero + 100)



print("19. Uma loja está com uma promoção de 10% desconto em compras acima de R$100. Faça um programa que receba um valor, calcule e imprima o valor do desconto, se existir, e o valor final da compra.")

valor = float(input("Valor: "))

if(valor > 100):
    print("Desconto de 10%: R$" '%')


print("20. Faça um programa que calcule o valor de imposto a ser pago a partir de um salário bruto. Se o salário for um valor até R$1.903,98, a pessoa não precisa pagar imposto de renda. Por outro lado, se o salário for menor que R$2.826,65 é cobrado 7,5% de imposto e se for maior, cobra-se 15%. Faça um programa que receba o salário bruto, calcule e mostre o valor a ser pago.")
print("21. Uma loja está com uma promoção em compras acima de R$500. Acima desse valor, a loja oferece 10% de desconto se o cliente pagar por PIX ou 5% de desconto para outras formas de pagamento. Por outro lado, para compras abaixo de R$500, a loja oferece apenas 5% de desconto se o pagamento for por PIX. Faça um programa que receba um valor e a forma de pagamento, calcule e imprima o valor do desconto e o valor final da compra")
print("22. Faça um Programa receba o valor de x, calcule e imprima o valor de f(x) que será:")
# f(x) = 1 / (2 - x) se x < 2
# f(x) = 1 / (x - 2) se x >= 2
print("23. Construa um programa que receba três valores, A, B e C. Em seguida, apresente na tela somente o maior deles")
print("24. Construa um programa para receber quatro números e no final apresentar o maior e o menor")