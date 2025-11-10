n = int(input("Digite um número: "))

fatorial = 1
i = n

while i > 1:
    fatorial *= i   # multiplica o resultado pelo número atual
    i -= 1          # diminui o contador

print(f"O fatorial de {n} é {fatorial}")
