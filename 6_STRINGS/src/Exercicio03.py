#Verificar se uma palavra é palíndromo (ex: “arara”).

palavra = "arara"
def is_palindromo(palavra):
    return palavra == palavra[::-1]

    print(is_palindrome("arara"))
if is_palindromo(palavra):
    print(f"{palavra} é palíndromo")
else:
    print(f"{palavra} não é palíndromo")
