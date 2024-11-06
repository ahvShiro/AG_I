import random as r

# Lista – Funções com retorno

# Crie um arquivo separado para você colocar todas as funções criadas. Para testar e utilizar as funções, crie um arquivo principal e importe o arquivo criado para as funções.

# 1. Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado 
# pelo usuário, utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.
def pedir_int():
    return int(input("Digite um número inteiro: "))


# 4. Faça uma função para gerar números aleatórios. Esta função deve receber um número inteiro por parâmetro e retornar um número 
# aleatório entre 1 e ele. Assim, toda vez que você precisar de um número qualquer pode usar a função do exercício 1 ou esta.

def gerar_aleatorio(num):
    return r.randint(1, num)


# 5. Crie duas funções para sortear números aleatórios. As funções devem receber o limite inferior e o superior por parâmetros. 
# Uma função deve retornar um número par e a outra um número ímpar. Detalhe: uma função não pode ser criada dentro de outra.

def aleatorio_par(min, max):
    while(True):
        random_int = r.randint(min, max)
        if((random_int % 2) == 0):
            return random_int

def aleatorio_impar(min, max):
    while(True):
        random_int = r.randint(min, max)
        if((random_int % 2) != 0):
            return random_int

# 6. Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne a mensagem “Mês inválido”.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def mes_extenso(num):
    if(num <= 1 and num >= 12 ):
        return(meses[int - 1])
    else:
        return("número inválido")


# 7. Faça funções para resolver as equações de área:
# do quadrado = x²  

def area_quadrado(num):
    return(num * num)

# do retângulo = b . h 	(base x altura)
def area_retangulo(base, altura):
    return(base * altura)

# do triângulo= (b . h)2
def area_triangulo(base, altura):
    return((base * altura) / 2)

# do trapézio = (B + b) . h2
def area_trapeziol(base_maior, base_menor, altura):
    return(((base_maior + base_menor) * altura ) / 2)


# Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que n! depende de (n-1)!; 
# este por sua vez depende de (n-2)!; 
# e, assim por diante, até que n seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. 
# Utilize uma função que recebe como parâmetro o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.

def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return(resultado)


# %% Faça uma função que receba um vetor como parâmetro e retorne apenas o maior valor deste vetor.
def ordenar(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while(j >= 0 and vetor[j] > chave):
            vetor[j + 1] = vetor[j]
            j -= 1 
        vetor[j + 1] = chave
    return(vetor)





# Faça uma função que receba um vetor como parâmetro e retorne apenas o menor valor deste vetor.
# Faça uma função para receber um vetor como parâmetro, calcular a soma desse vetor e retornar apenas a média dos valores.
# Faça uma função que recebe um vetor de números inteiros como parâmetro. Esta função deve calcular o dobro de cada valor do vetor e retornar um vetor inteiro atualizado com o dobro de cada número. Dica: crie outro vetor dentro da função com o mesmo tamanho para preencher com o dobro. 
# Construa uma função que receba por parâmetro uma data no formato DD/MM/AAAA e devolva uma string no formato DD de Mês Por Extenso de AAAA. Para pegar o mês por extenso, utilize a função criada no exercício 3. Por exemplo: 18/09/2019 retorna 18 de Setembro de 2019.
# Faça uma função que retorne o reverso de um número inteiro informado por parâmetro. Por exemplo: 127 retorna 721.
# Faça uma função que recebe uma frase (ou palavra) por parâmetro e retorne essa frase invertida. Por exemplo: Rafael retorna leafaR
# Faça uma função que recebe uma frase (ou palavra) por parâmetro e retorne quantas vogais essa frase tem. Por exemplo: se a frase for “Rafael” a função retorna 3
# Construa uma função que receba uma string como parâmetro e retorne outra string com os caracteres embaralhados. Por exemplo: se a função receber a palavra “Python”, pode retornar “npthyo”, “ophtyn” ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
# Refaça o exercício anterior, porém sem repetir os caracteres. Exemplo: com a string “Python” não se pode ter como retorno “nhtohpy” com caracteres repetidos (a não ser que a palavra contenha caracteres repetidos, como Rafael).
# Crie uma função para gerar senhas aleatórias com letras, números e caracteres especiais. A função deve receber o tamanho da senha (quantidade de caracteres) e retornar uma senha aleatória com esse tamanho podendo conter letras minúsculas, maiúsculas, números ou caracteres especiais (!@#$%&*()-+[{]}?). Por exemplo: se o tamanho for 8 a função deve retornar uma senha com 8 caracteres, como: a8B&Om1j.
# Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário.
# O percentual de aumento deve ser consultado por meio de uma função que recebe por parâmetro o cargo e retorna o percentual de aumento.
# Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber só 5% de aumento. 
# Por fim, mostre o salário antigo, o novo salário e a diferença. 
# Cargo
# Percentual
# Gerente
# 10%
# Engenheiro
# 20%
# Técnico
# 30%


# Crie uma função para calcular o fatorial, mas não utilize laço de repetição e sim recursividade (função chamando ela mesmo).


# %%
