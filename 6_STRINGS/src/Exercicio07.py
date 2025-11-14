nome = input("Digite seu nome completo: ").strip()

partes = nome.split()

primeiro = partes[0]
ultimo = partes[-1]

print("Primeiro nome:", primeiro)
print("Último nome:", ultimo)
