# Abre o arquivo para escrita - adicionar texto
arq = open("amigos.txt", "a", encoding="UTF-8")

# Pede dados par o usuário
nome = input("Nome do amigo: ")
idade = int(input("Idade do amigo: "))

"""Escrevendo dados no arquivo"""
# Modo Noob - Opção 1
arq.write(nome)
arq.write(", ")
arq.write(str(idade))
arq.write("\n")

# Modo estudante - Opção 2
tudo = nome + ", " + str(idade) + "\n"
arq.write(tudo)

# Modo Pro - Opção 3
tudo = f"{nome}, {idade}\n"
arq.write(tudo)

# Fecha o arquivo
arq.close()
