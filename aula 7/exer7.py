import os
def sizeFiles(direct):
    quantos = os.listdir(direct)
    lst = []
    for a in range(len(quantos)):
        size = os.stat(quantos[a]).st_size
        lst.append((quantos[a],size))
    return lst
print(sizeFiles("diretorio em que se procura"))

"""
Primeiro pomos os ficheiros como sendo uma lista. vemos o tamanho desse ficheiro
e ent\ao acrescentamos esse tuplo a uma lista
ate se pode colocar um if para que caso haja uma pasta dentro dessa pasta ent 
se volte a chamar a função e adicione à lista
"""
