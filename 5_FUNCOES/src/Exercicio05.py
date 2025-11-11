def numeroPar(a):
    if a % 2 == 0:
        return True
    else:
        return False

# Testando vários números
print(numeroPar(1))  # False
print(numeroPar(2))  # True
print(numeroPar(7))  # False
print(numeroPar(8))  # True
