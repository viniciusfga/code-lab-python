compra = float(input("Valor da compra: R$ "))

if 0 <= compra <= 100:
    novo_preco = compra * 0.95   # 5% de desconto
    print(f"Valor com desconto: R$ {novo_preco:.2f}")

elif 101 <= compra <= 500:
    novo_preco = compra * 0.90   # 10% de desconto
    print(f"Valor com desconto: R$ {novo_preco:.2f}")

elif compra > 500:
    novo_preco = compra * 0.85   # 15% de desconto
    print(f"Valor com desconto: R$ {novo_preco:.2f}")

else:
    print("Valor inválido! A compra não pode ser negativa.")
