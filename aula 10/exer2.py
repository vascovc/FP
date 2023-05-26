with open("lusiadas.txt") as ficheiro:
    dicionario = {}
    for line in ficheiro:
        for caracter in line:
            if str.isalpha(caracter):
                letra = str.lower(caracter)
                if letra in dicionario:
                    dicionario[letra] += 1
                else:
                    dicionario[letra] = 1
    for item in dicionario.sorted(key = dicinario[item], reverse=True):
        print(item,dicionario[item])
"""
Esta primeira parte é cópia do exercicio 2 da aula 8

O que varia é o print em que organizamos o dicionario pelos valores
e como se quer do maior para o mais pequeno faz-se o reverse
"""
