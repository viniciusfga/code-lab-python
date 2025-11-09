# Variáveis iniciais
numero_int = 10
numero_float = 3.75
texto_numero = "25"

# Conversões
int_para_float = float(numero_int)
float_para_int = int(numero_float)
str_para_int = int(texto_numero)
int_para_str = str(numero_int)

# Exibição dos resultados
print("Conversão int → float:", int_para_float, "| Tipo:", type(int_para_float))
print("Conversão float → int:", float_para_int, "| Tipo:", type(float_para_int))
print("Conversão str → int:", str_para_int, "| Tipo:", type(str_para_int))
print("Conversão int → str:", int_para_str, "| Tipo:", type(int_para_str))
