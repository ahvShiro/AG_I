# Lista – Funções

# %% Exercício 1: Análise de Notas de Estudantes
# Contexto: Uma escola quer calcular a média das notas dos alunos de uma turma e identificar se 
# algum aluno obteve uma nota abaixo da média. Crie uma função que calcule a média das notas de 
# todos os alunos e, em seguida, retorne uma lista com o nome dos alunos cujas notas estão abaixo 
# da média.
# Enunciado: Crie uma função verificar_notas_abaixo_da_media(notas, nomes) que recebe duas listas:
# notas: uma lista com as notas dos alunos.
# nomes: uma lista com os nomes dos alunos.
# A função deve calcular a média das notas e retornar uma lista com os nomes dos alunos cujas notas estão abaixo da média.
# Exemplo de uso:
# notas = [7, 4, 9, 6, 5]
# nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]
# print(verificar_notas_abaixo_da_media(notas, nomes))
# # Saída esperada: ['Maria', 'Ana', 'Lucas']

def verificar_notas_abaixo_da_media(notas: list, nomes: list) -> list:
    soma = 0

    for i in range(0, len(notas)):
        soma += notas[i]
    
    media = soma / len(notas)

    total_abaixo_media = 0

    for i in range(0, len(notas)):
        if notas[i] < media:
            total_abaixo_media += 1
    
    alunos_abaixo_media = [""] * total_abaixo_media

    j = 0

    for i in range(0, len(notas)):
        if notas[i] < media:
            alunos_abaixo_media[j] = nomes[i]
            j += 1

    return alunos_abaixo_media


# %% Exercício 2: Controle de Estoque de Produtos
# Contexto: Uma loja de eletrônicos possui um sistema de controle de estoque onde cada produto tem um código, uma quantidade em estoque 
# e um preço unitário. O gerente quer saber o valor total em estoque para cada produto.

# Enunciado: Crie uma função calcular_valor_estoque(codigos, quantidades, precos) que recebe três listas:

# codigos: uma lista com os códigos dos produtos.
# quantidades: uma lista com as quantidades em estoque para cada produto.
# precos: uma lista com os preços unitários de cada produto.

# A função deve retornar uma lista com o valor total em estoque para cada produto (quantidade * preço unitário).

# Exemplo de uso:
# codigos = ["A001", "A002", "A003"]
# quantidades = [10, 5, 8]
# precos = [200.0, 150.0, 120.0]
# print(calcular_valor_estoque(codigos, quantidades, precos))
# # Saída esperada: [2000.0, 750.0, 960.0]

def calcular_valor_estoque(codigos: list, quantidades: list, precos: list) -> list:
    valor_total_em_estoque = [0.0] * len(quantidades)

    for i in range(0, len(quantidades)):
        valor_total_em_estoque[i] = quantidades[i] * precos[i]
    
    return valor_total_em_estoque

codigos = ["A001", "A002", "A003"]
quantidades = [10, 5, 8]
precos = [200.0, 150.0, 120.0]
print(calcular_valor_estoque(codigos, quantidades, precos))
# Saída esperada: [2000.0, 750.0, 960.0]
        



# %% Exercício 3: Análise de Temperaturas em Diferentes Cidades
# Contexto: Uma estação meteorológica registra as temperaturas médias diárias de diferentes cidades. 
# O analista quer saber quantos dias a temperatura foi superior a uma certa referência em cada cidade.

# Enunciado: Crie uma função dias_acima_referencia(temperaturas, referencia) que recebe duas listas:
# temperaturas: uma lista com as temperaturas médias diárias de uma cidade durante uma semana (7 dias).
# referencia: um número que representa a temperatura de referência.
# A função deve retornar o número de dias em que a temperatura foi superior à referência.
# Exemplo de uso:
# temperaturas = [30, 32, 35, 28, 33, 31, 30]
# referencia = 31
# print(dias_acima_referencia(temperaturas, referencia))
# # Saída esperada: 4


def dias_acima_referencia(temperaturas:list, referencia:int) -> int:
    acima_ref = 0

    for i in range(0, len(temperaturas)):
        if temperaturas[i] > referencia:
            acima_ref += 1
    
    return acima_ref

temperaturas = [30, 32, 35, 28, 33, 31, 30]
referencia = 31
print(dias_acima_referencia(temperaturas, referencia))



# %% Exercício 4: Gestão de Salários de Funcionários
# Contexto: Uma empresa quer saber qual é o salário médio dos seus funcionários e 
# identificar os funcionários que ganham acima da média.
# Enunciado: Crie uma função salarios_acima_media(salarios, nomes) que recebe duas listas:
# salarios: uma lista com os salários dos funcionários.
# nomes: uma lista com os nomes dos funcionários.
# A função deve calcular a média dos salários e retornar uma lista com os nomes dos funcionários que ganham acima da média.
# Exemplo de uso:
# salarios = [3000, 2500, 5000, 4000, 3200]
# nomes = ["Carlos", "Maria", "Pedro", "Ana", "Luiza"]
# print(salarios_acima_media(salarios, nomes))
# # Saída esperada: ['Carlos', 'Pedro', 'Ana']

def salarios_acima_media(salarios: list, nomes: list) -> list:
    soma = 0

    for i in range(0, len(salarios)):
        soma += salarios[i]
    
    media = soma / len(salarios)

    total_acima_media = 0

    for i in range(0, len(nomes)):
        if salarios[i] > media:
            total_acima_media += 1
    
    salarios_acima = [""] * total_acima_media

    j = 0
    for i in range(0, total_acima_media):
        if salarios[i] < media:
            salarios_acima[j] = nomes[i]
            j += 1

    return salarios_acima

salarios = [3000, 2500, 5000, 4000, 3200]
nomes = ["Carlos", "Maria", "Pedro", "Ana", "Luiza"]
print(salarios_acima_media(salarios, nomes))
# Saída esperada: ['Carlos', 'Pedro', 'Ana']



# %% Exercício 5: Gestão de Vendas de um E-commerce
# Contexto: Um e-commerce deseja analisar o total de vendas por categoria de produto. 
# Para isso, ele possui uma lista com o valor de cada venda e outra lista com a categoria do produto vendido. 
# O gerente quer calcular o total de vendas de cada categoria.

# Enunciado: Crie uma função total_vendas_por_categoria(vendas, categorias) que recebe duas listas:
# vendas: uma lista com os valores de vendas realizadas.
# categorias: uma lista com as categorias dos produtos vendidos.

# A função deve retornar um dicionário onde as chaves são as categorias e os valores são o total 
# de vendas para cada categoria.

# Exemplo de uso:
# vendas = [150, 200, 350, 400, 250, 300]
# categorias = ["Eletrônicos", "Roupas", "Eletrônicos", "Móveis", "Roupas", "Eletrônicos"]
# print(total_vendas_por_categoria(vendas, categorias))
# # Saída esperada: {'Eletrônicos': 800, 'Roupas': 450, 'Móveis': 400}

# def total_vendas_por_categoria(vendas: list, categorias: list) -> dict:

