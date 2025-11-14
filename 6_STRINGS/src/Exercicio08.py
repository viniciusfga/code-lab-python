def criptografar(texto):
    mapa = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'A': '5',
        'E': '6',
        'I': '7',
        'O': '8'
    }

    resultado = ""

    for letra in texto:
        if letra in mapa:
            resultado += mapa[letra]
        else:
            resultado += letra

    return resultado

mensagem = input("Digite uma mensagem para criptografar: ")
criptografada = criptografar(mensagem)
print("Criptografado:", criptografada)
