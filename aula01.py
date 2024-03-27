print("Hello world!")

# === TIPOS DE DADOS ============================

# Inteiro
#   int() : Função para conversão
#   Sem vírgula
#   50, 45, -13584

# Ponto Flutuante
#   float()
#   Casas decimais separadas POR PONTOS [.]
#   3.14159265, 14.3, -50.5

# Booleano
#   bool() : Função para conversão
#   V ou F
#   True, False

# Strings
#   str() : Função para conversão
#   Cadeia de caracteres
#   "Bom dia", "Hello world", "Pindamonhangaba"

# Chars
#   Sem tipo de dado específico
#   'A', '@', ' '


# === VARIÁVEIS =================================

# Serve para armazenar dados de forma simples
#   Começa com letra minúscula
#   Sem espaços
#   Sem caracteres especiais
#   Não pode começar com número
#   snake_case, camelCase, kebab-case, PascalCase
#   Não pode ser reservado 

# nome_da_variavel = valor


# === EXERCÍCIO 1 ===============================

# Criar:
#   Uma variável que armazene a sua idade;
idade = 18

#   Uma variável que armazene o seu nome;
nome = "Nome "

#   Uma variável que armazene o seu sobrenome;
sobrenome = "Sobrenome"

#   Uma variável que armazene o seu nome completo, formado pela concatenação do seu nome pelo seu sobrenome (use as variáveis);
nome_completo = str(nome) + str(sobrenome)

#   Uma variável que contenha a sua altura;
altura = 180

#   Uma variável que contenha o seu peso;
peso = 80

#   Uma variável que contenha quantos dias na semana você estuda algoritmos;
dias_estudando = 8

#   Uma variável que indique se a luz do seu quarto está acesa ou apagada;
luz_quarto = False

# === EXERCÍCIO 2 ===============================
# Utilize o exercício anterior, apresentando na tela mensagens para cada valor de variável
print("Seu nome é " + str(nome))
print("Seu sobrenome é " + str(sobrenome))
print("Seu nome completo é " + str(nome_completo))
print("Sua altura é", int(altura))
print("Seu peso é", float(peso))
print("Você passa", int(dias_estudando), "dias por semana estudando algoritmos")
print("A luz do seu quarto está ligada:", bool(luz_quarto))