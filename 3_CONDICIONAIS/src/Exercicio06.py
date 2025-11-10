peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Obesidade grau I.")
elif imc < 40:
    print("Obesidade grau II (severa).")
else:
    print("Obesidade grau III (mórbida).")
