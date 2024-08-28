import random
import time

# even_nums = 0
# odd_nums = 0
# multiple_of_three = 0

# total_sum = 0
# average = 0
# iterations = 0

# for i in range(30):
#     num = random.randint(0, 100)
#     if(num == 50):
#         break
#     if(num % 5 == 0):
#         continue


# average = round((total_sum / iterations), 2)

# print(f"Quantidade de pares: {even_nums}")
# print(f"Quantidade de ímpares: {odd_nums}")
# print(f"Múltiplos de 3: {multiple_of_three}")
# print(f"Soma de todos: {total_sum}")
# print(f"Média: {average}")




# x = [0] * 5

# print(len(x))

# nome = input("string: ")

# print(len(nome))

# print(x[0])
# print(nome[len(nome) - 1])


tamanho_vetor = int(input("Digite a quantidade de alunos na sala: "))

chamada = [" "] * tamanho_vetor
for i in range(0, len(chamada)):
    chamada[i] = input("Seu nome: ")

print("== Alunos ==")

for nome in chamada:
    print(nome)

random.shuffle(chamada)

print("============")


qt_premios = int(input("Quantos prêmios serão sorteados? "))


for i in range(1, qt_premios + 1):
    input(f"O {i}º sorteio será realizado. Pressione enter para prosseguir... ")

    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    aluno_sorteado = random.randint(0, len(chamada) - 1)

    print(f"Parabéns {chamada[aluno_sorteado]}, você ganhou um prêmio surpresa!")