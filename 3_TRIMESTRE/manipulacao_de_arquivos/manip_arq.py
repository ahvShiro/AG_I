# # %% Read in file

# f = open("manipulacao_de_arquivos/doc.txt", "r", encoding="UTF-8")

# conteudo = f.readlines()

# # print(conteudo)

# for i in range(0, len(conteudo)):
#     linha = conteudo[i].replace("\n", "").split(", ")

#     if(int(linha[1]) >= 20):
#         print(f"Olá, {linha[0]}")

# f.close()

# %% Write in file

f = open("manipulacao_de_arquivos/doc.txt", "a", encoding="UTF-8")

nome = input("Nome: ")
idade = int(input("Idade: "))

f.write(f"{nome}, {idade}\n")
f.close()


f = open("manipulacao_de_arquivos/doc.txt", "r", encoding="UTF-8")
conteudo = f.readlines()

for i in range(0, len(conteudo)):
    linha = conteudo[i].replace("\n", "")
    print(linha)
f.close()