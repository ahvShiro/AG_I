matriz = [
            [0, 0, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 0]
        ]

print("Diagonal principal:")
for i in range(0, len(matriz)):
    print(matriz[i][i], end=' ')
print("\n")


print("Diagonal secundária:")

# 0, 3
# 1, 2
# 2, 1
# 3, 0
for i in range(0, len(matriz)):
    for j in range(len(matriz)-1, -1, -1):
        print(matriz[i][j], end=' ')
print("\n")