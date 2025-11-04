# 🐍 Guia de Exercícios — Parte III

Esta última parte do projeto **Learning Python** foca em estruturas de dados compostas, manipulação de arquivos e pequenos projetos aplicados.  
Aqui, o objetivo é consolidar os conhecimentos adquiridos e aplicá-los em problemas práticos do dia a dia da programação.

---

## 📚 Módulo 07 - Listas, Tuplas e Dicionários
📘 **Nível 1: Estruturas de Dados Compostas (54–65)**  
🔹 *Objetivo: compreender e manipular coleções em Python, utilizando listas, tuplas e dicionários para armazenar e processar informações.*

1. Criar uma **lista de números inteiros** e exibir todos os elementos.  
2. Adicionar um novo elemento ao final da lista com `append()`.  
3. Remover um elemento específico com `remove()`.  
4. Ordenar a lista em **ordem crescente e decrescente**.  
5. Verificar se um **valor está presente** na lista.  
6. Criar uma **tupla** com os dias da semana e exibir o terceiro dia.  
7. Criar um **dicionário** com informações de uma pessoa (nome, idade, cidade).  
8. Adicionar e remover chaves em um dicionário.  
9. Iterar sobre as **chaves e valores** de um dicionário.  
10. Exibir o **maior e menor valor** de uma lista numérica.  
11. Criar uma **lista de dicionários** representando produtos com nome e preço.  
12. 💡 *Desafio:* Criar um programa que **calcula a média de notas** usando uma lista e exibe a situação final (aprovado/reprovado).

📘 *Exemplo prático:*
```python
alunos = {"Ana": 8.5, "João": 7.2, "Carlos": 5.9}
for nome, nota in alunos.items():
    print(f"{nome} - Nota: {nota}")
```

---

## 📂 Módulo 08 - Arquivos
📘 **Nível 1: Persistência de Dados (66–72)**  
🔹 *Objetivo: aprender a manipular arquivos `.txt` e `.csv`, salvando e recuperando dados em Python.*

1. Criar um arquivo `.txt` e escrever uma mensagem dentro dele.  
2. Ler e exibir o conteúdo de um arquivo `.txt`.  
3. Escrever várias linhas em um arquivo usando um laço `for`.  
4. Criar um arquivo `.csv` com nomes e idades.  
5. Ler um arquivo `.csv` e imprimir cada linha formatada.  
6. Contar quantas linhas existem em um arquivo de texto.  
7. 💡 *Desafio:* Criar um programa que **salva e lê um histórico de notas** em um arquivo `.txt`.

📘 *Exemplo prático:*
```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Python é divertido!\n")

with open("dados.txt", "r") as arquivo:
    print(arquivo.read())
```

---

## 🧠 Módulo 09 - Projetos Pequenos
📘 **Nível 1: Aplicações Práticas (73–77)**  
🔹 *Objetivo: aplicar todos os conceitos aprendidos em mini projetos funcionais.*

1. Criar uma **Calculadora Interativa** com funções separadas para cada operação.  
2. Desenvolver um **Jogo de Adivinhação**, onde o usuário tenta acertar um número aleatório.  
3. Criar um **Gerador de Senhas Aleatórias** com letras, números e símbolos.  
4. Criar um **Conversor de Unidades** (temperatura, moedas ou distâncias).  
5. 💡 *Desafio:* Montar um **Sistema de Cadastro Simples**, armazenando dados em arquivo `.csv`.

📘 *Exemplo prático:*
```python
import random

numero = random.randint(1, 10)
palpite = int(input("Adivinhe o número (1 a 10): "))
if palpite == numero:
    print("🎉 Parabéns! Você acertou!")
else:
    print(f"😅 Errou! O número era {numero}.")
```

---

# 🧭 Índice de Exercícios — Parte III

### 📂 Módulo 07 - Listas, Tuplas e Dicionários
1. [Exercício 54: Criar uma lista e imprimir seus elementos](./7_ED_DICIONARIOS/src/Exercicio54.py)
2. [Exercício 55: Adicionar e remover elementos de uma lista](./7_ED_DICIONARIOS/src/Exercicio55.py)
3. [Exercício 56: Ordenar e inverter uma lista](./7_ED_DICIONARIOS/src/Exercicio56.py)
4. [Exercício 57: Verificar se um elemento está presente em uma lista](./7_ED_DICIONARIOS/src/Exercicio57.py)
5. [Exercício 58: Trabalhar com tuplas e exibir índices](./7_ED_DICIONARIOS/src/Exercicio58.py)
6. [Exercício 59: Criar e acessar elementos de um dicionário](./7_ED_DICIONARIOS/src/Exercicio59.py)
7. [Exercício 60: Atualizar valores em um dicionário](./7_ED_DICIONARIOS/src/Exercicio60.py)
8. [Exercício 61: Iterar sobre chaves e valores de um dicionário](./7_ED_DICIONARIOS/src/Exercicio61.py)
9. [Exercício 62: Combinar listas em um dicionário com zip()](./7_ED_DICIONARIOS/src/Exercicio62.py)
10. [Exercício 63: Contagem de ocorrências em lista usando dicionário](./7_ED_DICIONARIOS/src/Exercicio63.py)
11. [Exercício 64: Desafio — Sistema simples de cadastro com lista e dicionário](./7_ED_DICIONARIOS/src/Exercicio64.py)

---

### 📂 Módulo 08 - Arquivos
1. [Exercício 65: Criar e escrever em um arquivo .txt](./8_ARQUIVOS/src/Exercicio65.py)
2. [Exercício 66: Ler e exibir o conteúdo de um arquivo .txt](./8_ARQUIVOS/src/Exercicio66.py)
3. [Exercício 67: Gravar várias linhas em um arquivo](./8_ARQUIVOS/src/Exercicio67.py)
4. [Exercício 68: Ler um arquivo linha por linha e contar palavras](./8_ARQUIVOS/src/Exercicio68.py)
5. [Exercício 69: Manipular dados em arquivo .csv](./8_ARQUIVOS/src/Exercicio69.py)
6. [Exercício 70: Desafio — Registrar e ler notas de alunos em arquivo .txt](./8_ARQUIVOS/src/Exercicio70.py)

---

### 📂 Módulo 09 - Projetos Práticos
1. [Projeto 01: Calculadora Simples](./Projetos/src/Projeto01_Calculadora.py)
2. [Projeto 02: Jogo de Adivinhação](./Projetos/src/Projeto02_JogoAdivinhacao.py)
3. [Projeto 03: Gerador de Senhas](./Projetos/src/Projeto03_GeradorSenhas.py)
4. [Projeto 04: Conversor de Unidades](./Projetos/src/Projeto04_ConversorUnidades.py)
5. [Projeto 05: Desafio — Bloco de Notas Simples](./Projetos/src/Projeto05_BlocoNotas.py)