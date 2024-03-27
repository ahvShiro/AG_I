
# Faça um Programa que mostre a mensagem "Alô mundo!" na tela.

print("Alô mundo!")


# Faça um Programa e crie variáveis para armazenar seu nome e sobrenome (em variáveis diferentes). 
# Apresente na tela uma mensagem de boas vindas com o nome e sobrenome do usuário.

nome = "Nome"
sobrenome = "Sobrenmome"

print("Bem vindo,", nome, sobrenome)


# Continue o exercício anterior e crie mais variáveis para armazenar (uma para cada): 
# sua idade, seu peso, sua altura e sua data de nascimento. 
# Por fim, apresente todos esses dados na tela dentro de um print só.

nome = "Nome"
sobrenome = "Sobrenmome"
idade = 18
peso = 80
altura = 1.80
data_de_nascimento = "01/02/2003"

print("Nome completo:", nome, sobrenome, "\nIdade:", idade,  "\nPeso:", peso, "\nAltura:", altura, "\nData de Nascimento:", data_de_nascimento)


# Faça um programa que peça um número e apresente na tela o antecessor e o sucessor dele.

numero = int(input("Digite um número: "))

print("Antecessor:", (numero - 1), "\nSucessor:", (numero + 1))


# Faça um programa que peça dois números e imprima a soma deles.

n1 = int(input("n1: "))
n2 = int(input("n2: "))

print(n1, "+", n2, "=", (n1 + n2))


# Faça um programa que peça dois números e apresente a média aritmética deles.

n1 = float(input("n1: "))
n2 = float(input("n2: "))

print("A média de", n1, "com", n2, "é", (n1 + n2) / 2)


# Faça um programa que peça três números e imprima o produto (multiplicação) deles.

n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

print(n1, "*", n2, "*", n3, "=", (n1 * n2) * n3)


# Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética.

n1 = float(input("Nota 1º Bimestre: "))
n2 = float(input("Nota 2º Bimestre: "))
n3 = float(input("Nota 3º Bimestre: "))
n4 = float(input("Nota 4º Bimestre: "))

print("A média das notas é", (n1 + n2 + n3 + n4) / 4)


# Faça um programa que converta metros para centímetros.

n1 = float(input("Valor em Metros: "))

print(n1, "m =", (n1 * 100), "cm")


# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

n1 = int(input("Raio do círculo: "))
valor_pi = float(input("Valor de pi: "))

print("Área =", valor_pi * (n1 * n1))


# Faça um programa que peça a medida do lado de um quadrado, calcule e mostre sua área. 
# Em seguida, mostre também o perímetro do quadrado para o usuário.

n1 = int(input("Lado do quadrado: "))

print("Área:", (n1 * n1), "\nPerímetro:", (n1 * 4))


# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no dia. 
# Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês (considerando 30 dias).

ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_por_dia = float(input("Quantas horas você trabalha por dia? "))
ganho_por_dia = ganho_por_hora * horas_por_dia

print("Por dia você ganha", "R$" + str(ganho_por_dia))
print("Por mês você ganha", "R$" + str(ganho_por_dia * 30))
