# 1. Crie procedimentos com parâmetros informados pelo usuário no programa principal:

# Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.

def somar(x, y):
    print(x + y)

# Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
def multiplicar(x, y):
    print(x * y)

# Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularRaiz(x):
    print(x ** (1/2))

# Faça um procedimento que calcule a potência de um número (XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularPotencia(x, y):
    print(x ** y)

# Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
def calcularTabuada(x):
    for i in range(1, 10 + 1):
        print(f"{i} x {x} = {i * x}")


x = int(input("x: "))
y = int(input("y: "))

print("Soma:")
somar(x, y)

print("Multiplicação:")
multiplicar(x, y)

print("Raiz:")
calcularRaiz(x)

print("Potência:")
calcularPotencia(x, y)

print("Tabuada:")
calcularTabuada(x)



# Crie procedimentos com parâmetros:
# Crie um procedimento que recebe um vetor de números inteiros por parâmetro. Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado. 
# Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o maior valor do vetor.
# Faça um procedimento chamada encontrarMenor() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o menor valor do vetor.

# Crie no programa principal um vetor e preencha com números. Em seguida, utilize as três funções criadas no exercício anterior.


