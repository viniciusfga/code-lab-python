def soma_lista(numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

# Testando
valores = [5, 10, 3, 2]
print(f"A soma dos valores é: {soma_lista(valores)}")
