
pares = 0
impares = 0

while True:
    n = int(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else :
        impares += 1

print(pares, "PARES")
print(impares, "IMPARES")