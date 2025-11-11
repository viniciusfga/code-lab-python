# Variável global
mensagem = "Olá do escopo global!"

def exibir_mensagem():
    # Variável local
    mensagem = "Olá do escopo local!"
    print(mensagem)  # Usa a variável local

exibir_mensagem()
print(mensagem)  # Usa a variável global
