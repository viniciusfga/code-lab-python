palavra = "python". lower()

vogais = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

for letra in palavra:
    if vogais.isalpha(): # É PALAVRA?
        if letra in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

print(qtd_vogais)
print(qtd_consoantes)
