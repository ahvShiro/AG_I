# v = [1, 3, 5, 7, 9, 11]
# 
# menor = 0
# maior = len(v) - 1
# x = int(input("x: "))
# 
# while(menor <= maior):
#     meio = int(menor + (maior - menor) / 2)
# 
#     if(v[meio] == x):
#         print(f"{x} está em [{meio}]")
#         break
#     
#     elif(v[meio] > x):
#         maior = meio - 1
#         print(f"{x} está antes do meio")
#     
#     elif(v[meio] < x):
#         menor = meio + 1
#         print(f"{x} está depois do meio")
#     
# else:
#     print("Valor não está no vetor")
# 
# 





def bubbleSort(v):
    for i in range(0, len(v) - 1):
        for j in range(0, len(v) - 1):
            if(v[j] > v[j + 1]):
                x = v[j]
                v[j] = v[j+1]
                v[j+1] = x
    return v

v = [5, 2, 3, 1, 4]

x = bubbleSort(v)

print(x)




def inverter(string: str) -> str:
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida