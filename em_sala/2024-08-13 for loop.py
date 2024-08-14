import random

even_nums = 0
odd_nums = 0
multiple_of_three = 0
total_sum = 0
average = 0

for i in range(30):
    num = random.randint(0, 100)

    if(num % 2 == 0):
        even_nums += 1
    else:
        odd_nums += 1

    if(num % 3 == 0):
        multiple_of_three += 1

    total_sum += num

average = round((total_sum / 30), 2)

print(f"Quantidade de pares: {even_nums}")
print(f"Quantidade de ímpares: {odd_nums}")
print(f"Múltiplos de 3: {multiple_of_three}")
print(f"Soma de todos: {total_sum}")
print(f"Média: {average}")

