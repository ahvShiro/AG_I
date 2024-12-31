
# 1 - Criar uma função que recebe por parâmetro um dicionário com os dados de uma nova venda e escreve no final do arquivo.
def insert_venda(venda: dict) -> int:
    arquivo = open('loja/loja.csv', 'a')
    
    fstring = f"\n{venda['nome']},{venda['data']},{venda['quantidade']},{venda['valor']}"
    
    arquivo.write(fstring)
    arquivo.close()

    return 0

# 2 - Criar uma função que recebe por parâmetro o nome de um cliente e retorna 
# um vetor de dicionários de vendas do cliente (pesquisar pelo nome ou parte dele).

def select_cliente(nome: str) -> list:
    f = open("loja/loja.csv")
    content = f.readlines()
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
    f = open('loja/loja.csv', 'r')
    content = f.readlines()

    for i in range(0, len(content)):
        linha = content[i].strip().split(",")

        total = {
            "quantidade": 0,
            "valor": 0
        }

        if(nome in linha[0]):
            total["quantidade"] += int(linha[2])
            total["valor"] += float(linha[3])

    return total
    

# 4 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um vetor de dicionários com todas as vendas desse período (pesquisar pelo número do mês e ano).
def select_mes(mes: int, ano: int) -> list:

    f = open('loja/loja.csv', 'r')
    content = f.readlines()

    total = []

    for i in range(1, len(content)):
        linha = content[i].strip().split(",")
        data_em_vetor = linha[1].split("-")
        print(data_em_vetor)

        if(int(data_em_vetor[0]) == int(ano) and int(data_em_vetor[1]) == int(mes)):
            total.append({
                "nome": linha[0],
                "data": linha[1],
                "quantidade": linha[2],
                "valor": linha[3]
            })

    return total


# 5 - Criar uma função que recebe por parâmetro um mês e um ano e retorna um dicionário com a quantidade de itens vendidos e o valor total de vendas desse período (pesquisar pelo número do mês e ano).
def select_mes_total(mes: int, ano) -> dict:
    f = open('loja/loja.csv', 'r')
    ln = f.readlines()

    total = {
        "quantidade": 0,
        "valor": 0
    }

    for i in range(1, len(ln)):
        arr_ln = ln[i].strip().split(",")
        data_em_vetor = arr_ln[1].strip().split("-")

        if(int(data_em_vetor[0]) == int(ano) and int(data_em_vetor[1]) == int(mes)):
            total["quantidade"] += int(arr_ln[2])
            total["valor"] += float(arr_ln[3])

    return total


def print_vector(vetor: list) -> int:
    print("[", end='')
    for i in range(0, len(vetor) - 1):
        print(vetor[i], end=', ')
    print(f"{vetor[len(vetor) - 1]}]")

    return 0