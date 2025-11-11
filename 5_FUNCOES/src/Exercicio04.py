
# Função que calcula o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc  # Retorna o resultado

# Programa principal
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altur"))

resultado = calcular_imc(peso, altura)
print(f"Seu IMC é {resultado:.2f}")