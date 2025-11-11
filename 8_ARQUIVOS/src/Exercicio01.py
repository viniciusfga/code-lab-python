# Abre (ou cria) um arquivo chamado "mensagem.txt" no modo de escrita ('w')
arquivo = open("mensagem.txt", "w")

# Escreve uma mensagem dentro do arquivo
arquivo.write("Olá, este é meu primeiro arquivo em Python!\n")
arquivo.write("Aprendendo a manipular arquivos com open() e write().")

# Fecha o arquivo (boa prática)
arquivo.close()

print("Arquivo criado e mensagem gravada com sucesso!")
