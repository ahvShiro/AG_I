# Abre o arquivo para leitura
arq = open("amigos.txt", "r", encoding="UTF-8")
# Lê todas as linhas e cria um vetor de strings
conteudo = arq.readlines()
# Fecha o arquivo
arq.close()

# Percorre o vetor com os dados
for i in range(0, len(conteudo)):
    # Obtém a linha i e tira o \n dela
    linha = conteudo[i].replace("\n", "")
    # Quebra a string onde tem a , e cria um vetor com os dados separados
    dados = linha.split(",")

    # Converte idade para inteiro    
    idade = int(dados[1])
    
    if(idade >= 30):
        print("Olá", dados[0])
        print("Você tem", dados[1], "anos.")
    
