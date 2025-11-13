#Verificar se uma palavra é palíndromo (ex: “arara”).

palavra = "arara"

def is_palindrome(palavra : str) -> bool:
    cleaned = ''.join(ch for ch in palavra.lower() if ch.isalnum())
    return cleaned == palavra[::-1]

if __name__ == '__main__':
    print(is_palindrome("arara"))
if is_palindrome(palavra):
    print(f"{palavra} é palíndromo")
else:
    print(f"{palavra} não é palíndromo")
