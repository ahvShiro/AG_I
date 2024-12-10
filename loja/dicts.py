
# 1 - Criar uma função que recebe por parâmetro um dicionário com os dados de uma nova venda e escreve no final do arquivo.
def insert_venda(venda: dict) -> int:
    arquivo = open('loja/loja.csv', 'a')
    
    fstring = f"{venda['nome']},{venda['data']},{venda['quantidade']},{venda['valor']}\n"
    
    arquivo.write(fstring)
    arquivo.close()

    print(fstring)
    return 0

# 2 - Criar uma função que recebe por parâmetro o nome de um cliente e retorna 
# um vetor de dicionários de vendas do cliente (pesquisar pelo nome ou parte dele).

def select_cliente(nome: str) -> list:
    f = open("loja/loja.csv")
    content = f.readlines()[1:]
    vendas = []

    for i in range(0, len(content)):
        # [nome, data, quantidade, valor]
        linha = content[i].strip().split(",")

        if(nome in linha[0]):
            vendas.append({
                "nome": linha[0],
                "data": linha[1],
                "quantidade": linha[2],
                "valor": linha[3]
            })

    f.close()
    return vendas




# 3 - Criar uma função que recebe por parâmetro o nome de um cliente e retorna um dicionário com a quantidade de itens vendidos e o valor total de vendas do cliente (pesquisar pelo nome ou parte dele).
def select_cliente_total(nome: str) -> list:
    return 1

# 4 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um vetor de dicionários com todas as vendas desse período (pesquisar pelo número do mês e ano).
def select_mes(mes: int, ano: int) -> list:
    return 1

# 5 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um dicionário com a quantidade de itens vendidos e o valor total de vendas desse período (pesquisar pelo número do mês e ano).
def select_mes_total(mes: int, ano) -> dict:
    return 1