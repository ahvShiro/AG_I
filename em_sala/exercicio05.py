# # Exercício 5

while True:
    passwd_lenght = len(input("Senha: "))
    if (passwd_lenght <= 5):
        print("Senha fraca")
    elif (passwd_lenght <= 10):
        print("Senha média")
    else:
        print("Senha forte")
        break

# Exercício 6

x = float(input("x: "))
y = float(input("y: "))
operator = input("Operador: ")

# Soma
if (operator == '+'):
    print(f"{x} + {y} = {x + y}")
# Subtração
elif (operator == '-'):
    print(f"{x} - {y} = {x - y}")
# Multiplicação
elif (operator == '*'):
    print(f"{x} * {y} = {x * y}")
# Divisão
elif (operator == '/'):
    print(f"{x} / {y} = {x / y}")
# Operador inválido
else:
    print("Operador inválido")





