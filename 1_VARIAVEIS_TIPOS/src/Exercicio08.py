nome = "Eduardo"
idade = 24
altura = 1.75
peso = 68.4

# Cálculo com formatação dentro da f-string
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f} — {'Peso normal' if 18.5 <= imc < 25 else 'Fora do peso ideal'}.")

# Exemplo de alinhamento e espaçamento
print(f"{'Nome':<10} | {'Idade':^6} | {'IMC':>5}")
print(f"{nome:<10} | {idade:^6} | {imc:>5.2f}")