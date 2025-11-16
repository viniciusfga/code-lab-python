lista = [2, 1, 3, 7, 5, 6, 4, 8, 9, 10]


print("ORDEM CRESCENTE")
lista.sort()
for item in lista:
    print(item, " ",end="")

print()
print("ORDEM DECRESCENTE")

lista.sort(reverse=True)
for item in lista:
    print(item, " ",end="")