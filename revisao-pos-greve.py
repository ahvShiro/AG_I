name = "Adalberto Pereira"
birthday = "21/03/2000"
age = 24
paycheck = 9999.9999999
acTurnedOn = False

def floatToBrl(float) -> str:
    return f"R$ {float:.2f}"

print(f"Nome: {name}, Aniversário: {birthday}, Idade: {age}, Salário: {floatToBrl(paycheck)}, O ar tá ligado?: {acTurnedOn}")
