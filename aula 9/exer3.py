"""with open("names.txt") as ficheiro:
	names = [line.strip() for line in ficheiro]
	tudo = []
	dici = {}
	for a in names:
		nomes = a.split(" ")
		tudo.append(nomes)
	for a in tudo:
		if a[-1] in dici:
			if a[0] not in dici[a[-1]]:
				dici[a[-1]].append(a[0])
		else:
			dici[a[-1]] = [a[0]]
	print(dici)
"""

"""
abrimos o ficheiro e vamos percorrer cada linha e adicionamos cada um desses
nomes todos a uma lista. Depois partimos esse nome em sublistas e assim ficamos
como cada parte do nome sendo um elemento da lista dentro de uma lista maior.
O processo que aqui ficou não foi o mais simples porque fazendo o split tinha sido mais simples

Vamos entao à lista com todos os nomes e se o ultimo nome nao estiver no dicionario adicionamos
se estiver entao temos que ver se o nome ja la esta pois se estiver nao interessa pois nao podem
aparecer repetidos

Aviso que este não e o melhor processo e não e aquilo que o professor queria porque aqui usei uma
lista e pela imagem conseguimos ver que nao foi isso o utilizado. no entanto isto funciona
E muito mais facil seria se considerarmos um set que elimina logo os repetidos
"""
def fun():
    with open("names.txt") as ficheiro:
        lista = []
        for line in ficheiro:
            lista.append(line.split())
        dic = {}
        for a in lista:
            if a[-1] not in dic:
                dic[a[-1]] = {a[0]}
            else:
                value = dic[a[-1]]
                nome = {a[0]}
                dic[a[-1]] = value.union(nome)
        return dic
print(fun())
