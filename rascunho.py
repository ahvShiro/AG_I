

# for i in range(altura):
#     # # SPACING
#     # for spacing in range(altura - j - 1):
#     #     print(" ", end="")
#     # # ROW
#     for j in range(i + 1):
#         print("#", end="")
#     # LINE BREAK
#     print()



altura = int(input("altura: "))

i = 0
while i < altura:
    j = 0
    while j <= i:
        print("#", end='')
        j += 1
    print()
    i += 1





