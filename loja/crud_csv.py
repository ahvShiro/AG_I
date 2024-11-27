# 1 - Criar uma função para adicionar uma linha com os dados necessários no arquivo.
def inserir_dados(nome:str, data:str, qt_items:str, valor:str) -> int:
    f = open("loja.csv", "a")
    f.write(f"{nome},{data},{qt_items},{valor}\n")
    f.close()
    return 0

# 2 - Criar uma função para listar todas as vendas de um cliente (pesquisar pelo nome ou parte dele).
def buscar_vendas_de_cliente(query: str) -> list:
    f = open("loja.csv")
    content = f.readlines()

    for i in range(0, len(content)):
        # [nome, data, quantidade, valor]
        linha = content[i].split(",").replace("\n", "")

        if(query in linha[0]):
            return(linha)

    f.close()


# 3 - Criar uma função para informar na tela a quantidade e o total de vendas de um cliente 
# (pesquisar pelo nome ou parte dele).
def imprimir_qt_e_venda_de_cliente(query: str, file="loja.csv"):
    f = open(file)
    content = f.readlines()

    for i in range(0, len(content)):
        # [nome, data, quantidade, valor]
        linha = content[i].split(",").replace("\n", "")

        if(query in linha[0]):
            return(linha)

    f.close()



# 4 - Criar uma função para listar todas as vendas de um mês específico 
# (pesquisar pelo número do mês).

# def listar_vendas_de_mes(numero_mes:str, file="loja.csv"):


# 5 - Criar uma função para informar a quantidade e o valor total de vendas de um mês específico 
# (pesquisar pelo número do mês).


