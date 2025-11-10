produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto em porcentagem: "))

novo_produto = produto - (produto * desconto / 100)

print(novo_produto)
