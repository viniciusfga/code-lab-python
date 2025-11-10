letra = input("Digite uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra.")
elif letra in "aeiou":
    print("É uma vogal.")
else:
    print("É uma consoante.")
