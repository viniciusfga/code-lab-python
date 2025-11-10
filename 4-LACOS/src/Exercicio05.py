soma = 0
cont = 0

while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break  # sai do laço antes de contar o 0
    soma += n
    cont += 1

# evita divisão por zero
if cont > 0:
    media = soma / cont
    print(f"Média = {media:.2f}")
else:
    print("Nenhum número foi digitado.")
