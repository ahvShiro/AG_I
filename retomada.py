name = "Adalberto Pereira"
birthday = "21/03/2000"
age = 24
paycheck = 2403.14159265358939323
acTurnedOn = False

def floatToBrl(float) -> str:
    return f"R$ {float:.2f}"

print(f"Nome: {name}, Aniversário: {birthday}, Idade: {age}, Salário: {floatToBrl(paycheck)}, O ar tá ligado?: {acTurnedOn}")
print("\\\"")