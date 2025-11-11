
def maior_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Testando
resultado = maior_de_tres(10, 5, 20)
print(f"O maior número é: {resultado}")
