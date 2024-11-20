# import crud_csv as csv
f = open("loja.csv")

content = f.readlines()

for i in range(0, len(content)):
    # [nome, data, quantidade, valor]
    linha = content[i].split(",").replace("\n", "")
    

f.close()




# 6 - Criar um menu principal com as opções acima
