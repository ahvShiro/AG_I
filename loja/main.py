# 6 - Criar um menu principal com as opções acima de modo que os dados obtidos 
# por meio do retorno das funções sejam exibidos adequadamente (for e não print(vetor)) na tela.

import dicts as d

d.select_mes(12, 2024)

while True:
    print("\nMenu:")
    print("1. Inserir venda")
    print("2. Listar vendas do cliente")
    print("3. Listar total de vendas do cliente")
    print("4. Listar vendas de um período")
    print("5. Listar total de vendas de um perídodo")
    print("6. Sair")
    print("\n")
    user_input = int(input("> Escolha uma opção: "))

    if(user_input == 1):
        print("dados = {")
        nome = input("    nome: ")
        data = input("    data: ")
        quantidade = int(input("    quantidade: "))
        valor = float(input("    valor: "))
        print("}")

        venda = {
            "nome": nome,
            "data": data,
            "quantidade": quantidade,
            "valor": valor
        }
        print("\n")
        d.insert_venda(venda)

    elif(user_input == 2):
        nome = input("Nome do cliente: ")
        vendas = d.select_cliente(nome)
        print("\n")

        d.print_vector(vendas)

    elif(user_input == 3):
        nome = input("Nome do cliente: ")
        total = d.select_cliente_total(nome)
        print("\n")

        print(total)

    elif(user_input == 4):
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        vendas = d.select_mes(int(mes), int(ano))
        print("\n")

        d.print(vendas)

    elif(user_input == 5):
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        total = d.select_mes_total(int(mes), int(ano))
        print("\n")

        print(total)

    elif(user_input == 6):
        print("\n")

        break

    else:
        print("\n")

        print("> Opção inválida\n")

