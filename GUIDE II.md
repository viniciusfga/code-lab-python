# 🐍 Guia de Exercícios — Parte II

Este guia reúne os exercícios dos módulos 4 a 6 do projeto **Learning Python**, voltados para o domínio das estruturas de repetição, modularização do código com funções e manipulação de strings.

---

## 🔁 Módulo 04 - Laços de Repetição
📘 **Nível 1: Iterações e Controle de Fluxo (26–35)**  
🔹 *Objetivo: compreender o funcionamento dos laços `for` e `while`, uso de contadores, acumuladores e repetições aninhadas.*

1. Exibir os números de **1 a 10** usando um laço `for`.
2. Criar uma **contagem regressiva** de 10 até 1 usando `while`.
3. Ler um número `N` e calcular a **soma dos números de 1 até N**.
4. Ler um número e exibir a **tabuada** correspondente (1 a 10).
5. Calcular a **média** de valores digitados até que o usuário digite 0.
6. Contar quantos **números pares e ímpares** foram digitados.
7. Calcular o **fatorial** de um número informado.
8. Exibir apenas os **números ímpares entre dois valores**.
9. Somar todos os **múltiplos de 3** entre 1 e 100.
10. Criar um **padrão de asteriscos** com laços aninhados, formando um triângulo:
    ```
    *
    **
    ***
    ****
    *****
    ```
💡 *Desafio:* Criar um programa que desenhe diferentes padrões geométricos (triângulo, quadrado e pirâmide) com `for`.

---

## 🧩 Módulo 05 - Funções
📘 **Nível 1: Modularização e Reuso de Código (36–45)**  
🔹 *Objetivo: aprender a declarar funções, utilizar parâmetros e valores de retorno, além de entender o escopo de variáveis.*

1. Criar e chamar uma **função simples** que imprime uma saudação.
2. Criar uma função que **recebe dois números** e exibe a soma.
3. Criar uma função que **retorna o dobro** de um número.
4. Criar uma função para **calcular o IMC** e retornar o resultado.
5. Criar uma função que **verifica se um número é par**.
6. Criar uma função com **parâmetro opcional** (ex: saudação com nome padrão).
7. Criar exemplos que mostrem o **escopo local e global** de variáveis.
8. Criar uma função que **retorna o maior entre três números**.
9. Criar uma função que **soma todos os valores** de uma lista.
10. 💡 *Desafio:* Criar uma **calculadora modularizada**, com funções separadas para soma, subtração, multiplicação e divisão.

📘 *Exemplo de função simples:*
```python
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a) ao Learning Python.")

saudacao("Vinícius")
```

---

## ✨ Módulo 06 - Strings
📘 **Nível 1: Manipulação e Fatiamento de Texto (46–53)**  
🔹 *Objetivo: dominar os principais métodos e operações com strings, incluindo fatiamento, substituição e análise de caracteres.*

1. Ler uma string e exibir **quantos caracteres** ela possui.
2. Converter o texto para **maiúsculas e minúsculas**.
3. Verificar se uma **palavra é palíndromo** (ex: “arara”).
4. Substituir uma **palavra específica** dentro de uma frase.
5. Contar **quantas vogais e consoantes** existem em uma palavra.
6. Exibir partes de um texto utilizando **fatiamento**.
7. Ler o **nome completo** e mostrar apenas o primeiro e último nome.
8. 💡 *Desafio:* Criar uma **criptografia simples**, substituindo letras por outras (ex: a→@, e→3, i→1, o→0).

📘 *Exemplo prático:*
```python
texto = "Python é incrível!"
print(texto.upper())   # PYTHON É INCRÍVEL!
print(texto[0:6])      # Python
print(texto.replace("incrível", "poderoso"))  # Python é poderoso!
```

---

## 🧭 Índice de Exercícios
*(continua abaixo com os links dos exercícios em seus respectivos módulos)*


# 🧭 Índice de Exercícios — Parte II

## 📂 Módulo 04 - Laços de Repetição
26. [Exercício 26: Contagem de 1 a 10 com for](./code-lab-python/4_LACOS/Exercicio26.py)
27. [Exercício 27: Contagem regressiva com while](./code-lab-python/4_LACOS/Exercicio27.py)
28. [Exercício 28: Soma de números de 1 a N](./code-lab-python/4_LACOS/Exercicio28.py)
29. [Exercício 29: Tabuada de um número](./code-lab-python/4_LACOS/Exercicio29.py)
30. [Exercício 30: Média de valores digitados até digitar 0](./code-lab-python/4_LACOS/Exercicio30.py)
31. [Exercício 31: Contar números pares e ímpares](./code-lab-python/4_LACOS/Exercicio31.py)
32. [Exercício 32: Fatorial de um número](./code-lab-python/4_LACOS/Exercicio32.py)
33. [Exercício 33: Exibir números ímpares entre dois valores](./code-lab-python/4_LACOS/Exercicio33.py)
34. [Exercício 34: Soma dos múltiplos de 3 entre 1 e 100](./code-lab-python/4_LACOS/Exercicio34.py)
35. [Exercício 35: Padrão de asteriscos com laços aninhados](./code-lab-python/4_LACOS/Exercicio35.py)

---

## 📂 Módulo 05 - Funções
36. [Exercício 36: Criar e chamar uma função simples](./code-lab-python/5_FUNCOES/Exercicio36.py)
37. [Exercício 37: Função com parâmetros](./code-lab-python/5_FUNCOES/Exercicio37.py)
38. [Exercício 38: Função que retorna o dobro de um número](./code-lab-python/5_FUNCOES/Exercicio38.py)
39. [Exercício 39: Função que calcula o IMC](./code-lab-python/5_FUNCOES/Exercicio39.py)
40. [Exercício 40: Função para verificar número par](./code-lab-python/5_FUNCOES/Exercicio40.py)
41. [Exercício 41: Função com parâmetros opcionais](./code-lab-python/5_FUNCOES/Exercicio41.py)
42. [Exercício 42: Escopo de variáveis (global vs local)](./code-lab-python/5_FUNCOES/Exercicio42.py)
43. [Exercício 43: Função que retorna o maior entre três números](./code-lab-python/5_FUNCOES/Exercicio43.py)
44. [Exercício 44: Função que soma uma lista de números](./code-lab-python/5_FUNCOES/Exercicio44.py)
45. [Exercício 45: Desafio — Calculadora modularizada](./code-lab-python/5_FUNCOES/Exercicio45.py)

---

## 📂 Módulo 06 - Strings
46. [Exercício 46: Contar caracteres de uma string](./code-lab-python/6_STRINGS/Exercicio46.py)
47. [Exercício 47: Converter texto para maiúsculas e minúsculas](./code-lab-python/6_STRINGS/Exercicio47.py)
48. [Exercício 48: Verificar se uma palavra é palíndromo](./code-lab-python/6_STRINGS/Exercicio48.py)
49. [Exercício 49: Substituir palavras em uma frase](./code-lab-python/6_STRINGS/Exercicio49.py)
50. [Exercício 50: Contar vogais e consoantes](./code-lab-python/6_STRINGS/Exercicio50.py)
51. [Exercício 51: Fatiamento de string — exibir partes do texto](./code-lab-python/6_STRINGS/Exercicio51.py)
52. [Exercício 52: Separar nome e sobrenome](./code-lab-python/6_STRINGS/Exercicio52.py)
53. [Exercício 53: Desafio — Criptografia simples com troca de letras](./code-lab-python/6_STRINGS/Exercicio53.py)
