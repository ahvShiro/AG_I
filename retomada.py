name = "Adalberto Pereira"
birthday = "21/03/2000"
age = 24
paycheck = 2403.14159265358939323
acTurnedOn = False

def floatToBrl(float) -> str:
    return f"R$ {float:.2f}"

print(f"Nome: {name}, Aniversário: {birthday}, Idade: {age}, Salário: {floatToBrl(paycheck)}, O ar tá ligado?: {acTurnedOn}")
print("\\\"")


# Exercício 3: Implemente um algoritmo que solicite um número inteiro ao usuário. 
# Em seguida, informe na tela uma mensagem dizendo se o número é par ou ímpar.

# User input
while True:
    userInt = int(input("Digite um número inteiro: "))
    if(isinstance(userInt, int)):
        break

def isEven(int) -> bool:
    if(int % 2 == 0):
        return True
    else:
        return False

if(isEven(userInt)):
    print("Número par")
else:
    print("Número ímpar")
