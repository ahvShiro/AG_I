def upside_down_pyramid(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print("*", end='')
        print("")

def pyramid(n) -> str:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end='')
        print("")



def rightside_pyramid(n) -> str:
    for i in range(1, n + 1):


        for j in range(i, n + 1):
            print(" ", end='')
        
        for k in range(1, i + 1):
            print("*", end='')


        print("")


num = int(input("Tamanho da pirâmide: "))
rightside_pyramid(num)


