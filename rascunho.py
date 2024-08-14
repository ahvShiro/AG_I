import random

par = 0
impar = 0
multiplo_de_tres = 0
soma_total = 0
media = 0
iteracoes_validas = 0

for i in range(30):
    num = random.randint(0, 100)

    # CONDIÇÕES QUE IGNORAM ITERAÇÕES
    if(num == 50):
        break
    if(num % 5 == 0):
        continue

    # CONDIÇÕES PARA SEREM IMPRESSAS
    if(num % 2 == 0):
        par += 1
    else:
        impar += 1
    if(num % 3 == 0):
        multiplo_de_tres += 1

    # SOMA DE VARIÁVEIS A CADA ITERAÇÃO
    soma_total += num
    iteracoes_validas += 1

media = round((soma_total / iteracoes_validas), 2)

print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares: {impar}")
print(f"Múltiplos de 3: {multiplo_de_tres}")
print(f"Soma de todos: {soma_total}")
print(f"Média: {media}")