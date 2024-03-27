# === BOOLEANOS ===============================

# True
# False


# === Comparação de Valores ===============================

# Operadores relacionais:

# x > y     Maior que
# x >= y    Maior ou igual a
# x < y     Menor que 
# x <= y    Menor ou igual a
# x == y    Igual a
# x != y    Diferente de


# Condicional:

# if(condição):
#   função_seguida_de_tab()
# elif(condição):
#   função_seguida_de_tab()
# else:
#   função_seguida_de_tab()


x = int(input("Numero inteiro: "))

if(x % 2 == 0):
    print("Par")
else:
    print("Ímpar")

y = int(input("Outro número: "))

if(y > 0):
    y = 1 / y
else:
    y = -1
