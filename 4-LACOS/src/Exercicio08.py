a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)