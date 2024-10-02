# size = int(input("Insira o tamanho do vetor: "))
# vector = [0] * size
# print(vector)

##################################################################

# alunos = [""] * 30
# alunos[0] = "Arthur Heiji Voos Shiroshima"

# i = int(input("Qual posição você quer acessar? "))
# alunos[i] = input("Qual é o seu nome? ")

# print(alunos)

# t = len(alunos)
# print(t)




vector = [0] * 10

while True:
    i = int(input("Digite um endereço para inserir um valor: "))
    if(i < 0 or i > (len(vector) - 1)):
        print(f"Endereço {i} inválido, tente novamente")
    else:
        break

vector[i] = int(input("Digite um valor: "))
print(vector)