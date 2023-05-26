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
    for key in sorted(dicionario.keys()):
        print("{} : {}".format(key, dicionario[key])
"""
Abrimos o ficheiro e criamos um dicionario para servir de despejo para os
valores. Vai se ler linha a linha e caracter a caracter. Se esse caracter
for uma letra entao convertemos a minuscula.
Caso essa letra ja esteja no dicionario ent adicionamos 1 ao numero de
ocorrencias, caso nao esteja colocamos essa letra no dicionario e com um
como sendo o numero de ocorrencias

Isto esta a dar erro de compilaçao mas esta tudo bem escrito, tanto quanto sei
"""
