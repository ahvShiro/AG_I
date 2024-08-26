import random


## 1) Faça um programa em Python utilizando o for (um programa pra cada um), que:
## a) Apresente os números de 1 a 100 (um por linha).

# for i in range(1, 101):
#     print(i)


## b) Apresente os números de 100 a 1 (um por linha).

# for i in range(100, 0, -1):
#     print(i)


## c) Apresente os números pares de 1 a 100 (um por linha).

# for i in range(2, 101, 2):
#     print(i)

## OU

# for i in range(1, 101):
#     if(i % 2 == 0):
#         print(i)


## d) Apresente os números ímpares de 1 a 100 (um por linha).

# for i in range(1, 101, 2):
#     print(i)

## OU

# for i in range(1, 101):
#     if(i % 3 == 0):
#         print(i)


## e) Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.

# soma = 0
# for i in range(1, 101):
#     soma += i
# print(soma)


## f) Faça a soma dos números de X a Y (informados pelo usuário), 
## desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).

# x = int(input("Valor de X (menor que Y):"))
# y = int(input("Valor de Y (maior que X):"))
# soma = 0

# for i in range(x, y + 1):
#     soma += i
# print(soma)


# # g) Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. 
# # Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120

# j = int(input("j: "))

# factorial = 1
# for i in range(1, j + 1):
#     factorial *= i

# print(factorial)


## 2) Faça um programa que leia 5 números e informe apenas o maior número.

# maior_numero = 0
# for i in range(1, 5 + 1):
#     numero_atual = int(input(f"Digite um número ({i}/5): "))
#     if(numero_atual > maior_numero):
#         maior_numero = numero_atual

# print(f"Maior número: {maior_numero}")


## 3) Faça um programa que leia 5 números e informe a soma e a média dos números.

# soma = 0
# iteracao_atual = 0

# for i in range(1, 5 + 1):
#     numero_atual = int(input(f"Digite um número ({i}/5): "))
#     soma += numero_atual
#     iteracao_atual += 1

# print(f"Soma: {soma} \nMédia: {soma / iteracao_atual}")


## 4) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# for i in range(1, 50 + 1):
#     if(i % 2 != 0):
#         print(i)


## 5) O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
## Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o 
## número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa 
## precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi 
## contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 
## 1 até 50 produtos, conforme o exemplo abaixo:

## Lojas Quase Dois - Tabela de preços
## 1 - R$ 1.99
## 2 - R$ 3.98
## ...
## 50 - R$ 99.50

# price = 1.99

# print("Loja Quase Dois - Tabela de preços")
# for i in range(1, 50 + 1):
#     print(f"{i} - R$ {price * i:.2f}")


## 6) Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 1 ao 10 para um número informado pelo usuário.

# n = int(input("Insira um número para tabuada: "))

# for i in range(1, 10 + 1):
#     print(f"{i} x {n} = {i * n}")


## 7) Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do X a Y para um número 
## informado pelo usuário (semelhante ao anterior, porém o usuário precisa informar três números).

# n = int(input("Insira um número para tabuada: "))
# comeco = int(input("Insira um número para começo da tabuada: "))
# final = int(input("Insira um número para final da tabuada: "))

# for i in range(comeco, final + 1):
#     print(f"{i} x {n} = {i * n}")


## 8) Faça um programa que gere e apresente na tela X números inteiros aleatórios no intervalo de -100 a 100,
## de modo que o valor de X seja informado pelo usuário. No final do programa, apresente na tela: (1) a soma
## dos números gerados, (2) quantos números são positivos, (3) negativos, (4) o maior número gerado, (5) o menor
## número gerado, (6) quantos são pares, (7) ímpares e (8) quantos são múltiplos de 3.

# x = int(input("Informe a quantidade de números aleatórios de -100 a 100: "))

# soma = 0
# positivos = 0
# negativos = 0
# maior_numero = 0
# menor_numero = 0
# qt_pares = 0
# qt_impares = 0
# qt_mult_tres = 0


# for i in range(x):
#     numero_aleatorio = random.randint(-100, 100)
#     soma += numero_aleatorio

#     if(numero_aleatorio > 0):
#         positivos += 1
#     else:
#         negativos += 1
    
#     if(numero_aleatorio > maior_numero):
#         maior_numero = numero_aleatorio
        
#     if(numero_aleatorio < menor_numero):
#         menor_numero = numero_aleatorio
    
#     if(numero_aleatorio % 2 == 0):
#         qt_pares += 1
#     else:
#         qt_impares += 1
    
#     if(numero_aleatorio % 3 == 0):
#         qt_mult_tres += 1

# print(f"Soma: {soma} \nNúmeros positivos: {positivos} \nNúmeros negativos: {negativos} \nMaior número: {maior_numero} \nMenor número: {menor_numero} \nPares: {qt_pares} \nÍmpares: {qt_impares} \nMúltiplos de 3: {qt_mult_tres}")


## Lista GERAL de estruturas de repetição
## Recomenda-se o uso do while para laços não contatos e for para laços contados

## 9) Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários 
## para executar cada operação. O programa será executado repetidamente até que o usuário passe 
## o número informado para sair do programa (opção).

# while True:
#     option = int(input("====== Menu Principal ======\n1. Fazer a tabuada do 1 ao 10 para um número X\n2. Apresentar os múltiplos de X entre 1 e 100\n3. Apresentar a soma dos números de 1 a X\n4. Sair do programa \n> "))
#     if(option >= 1 and option <= 4):
#         break

# if(option == 1):
#     x = int(input("x: "))
#     for i in range(1, 10 + 1):
#         print(f"{i} x {x} = {i * x}")

# elif(option == 2):
#     x = int(input("x: "))
#     for i in range(1, 100 + 1):
#         if(i % x == 0):
#             print(i)

# elif(option == 3):
#     x = int(input("x: "))
#     soma = 0
#     for i in range(1, x + 1):
#         soma += i
#     print(soma)

# elif(option == 4):
#     print("Saíndo...")
#     exit()


## 10) Crie um jogo simples onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve adivinhar o número. 
## Use um laço “while” para permitir que o usuário continue tentando até acertar. Após cada tentativa, informe se o palpite 
## é maior, menor ou igual ao número sorteado.

# numero_computador = random.randint(1, 100)

# while True:
#     numero_usuario = int(input("Adivinhe o número escolhido: "))
#     if(numero_usuario == numero_computador):
#         print("Parabéns, você acertou!")
#         break
#     elif(numero_usuario > numero_computador):
#         print(f"{numero_usuario} é maior que o número escolhido")
#     elif(numero_usuario < numero_computador):
#         print(f"{numero_usuario} é menor que o número escolhido")


## 11) Refaça o exercício anterior, porém utilize um laço “for” para limitar o número de tentativas a 10 (usuário tem 10 chances só para acertar).

# numero_computador = random.randint(1, 100)

# for i in range(1, 10+1):
#     numero_usuario = int(input(f"Adivinhe o número escolhido ({i}/10): "))
#     if(numero_usuario == numero_computador):
#         print("Parabéns, você acertou!")
#         break
#     elif(numero_usuario > numero_computador):
#         print(f"{numero_usuario} é maior que o número escolhido")
#     elif(numero_usuario < numero_computador):
#         print(f"{numero_usuario} é menor que o número escolhido")


## 12) Crie um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
## [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo. No final, apresente quantos números há em cada intervalo.


# zero_a_vinte_e_cinco = 0
# vinte_e_seis_a_cinquenta = 0
# cinquenta_e_um_a_setenta_e_cinco = 0
# setenta_e_seis_a_cem = 0

# while True:
#     user_input = int(input("Digite um número positivo: "))
#     if(user_input < 0):
#         print(f"[0-25]: {zero_a_vinte_e_cinco}, [26-50]: {vinte_e_seis_a_cinquenta}, [51-75]: {cinquenta_e_um_a_setenta_e_cinco}, [76-100]: {setenta_e_seis_a_cem}")
#         break
#     if(user_input < 25):
#         zero_a_vinte_e_cinco += 1
#     elif(user_input < 50):
#         vinte_e_seis_a_cinquenta += 1
#     elif(user_input < 75):
#         cinquenta_e_um_a_setenta_e_cinco += 1
#     elif(user_input < 100): 
#         setenta_e_seis_a_cem += 1


## 13) Desenvolva um programa que calcule o custo total de uma viagem com base na distância a ser percorrida e o tipo de veículo. O custo por 
## quilômetro varia conforme o tipo de veículo, conforme a tabela abaixo:
## Tipo de Veículo
## Custo por Quilômetro
## Econômico
## R$ 1,50
## Médio
## R$ 2,25
## Luxo
## R$ 3,00

## 14) O programa deve solicitar a distância a ser percorrida e o tipo de veículo. Em seguida, deve calcular e exibir o custo total da viagem. 
## O programa deve permitir que o usuário faça novos cálculos até que ele escolha encerrar.

