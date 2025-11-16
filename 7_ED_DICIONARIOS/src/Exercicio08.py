computador = {
    "modelo" : "Dell",
    "placa_grafica" : "Nvidia RTX"
}

computador["memoria_ram"] = 32
print(computador)

valor_removido = computador.pop("modelo")
print(computador)
print(valor_removido)