def converter():
    with open("stocks.csv") as ficheiro:
        lista = []
        lst = []
        lstaa = []
        for line in ficheiro:
            linha = line.strip()
            nome,data,preçoabertura,preçomaximo,preçominimo,preçofecho,volume = linha.split(",")
            tuplo = nome,data,preçoabertura,preçomaximo,preçominimo,preçofecho,volume
            lista.append(tuplo)
        for a in range(1,len(lista)):
            if lista[a][0] == lista[a-1][0]:
                lst.append(lista[a])
            else:
                lstaa.append(lst)
                lst = []
        print(lstaa)
        return lista,lstaa
"""
Esta funçao serve para abrir o ficheiro e passar os valores para uma lista
o segundo for serve para se dividir em sublistas por causa de haverem de empresas
com o mesmo nome assim essas estao divididas
"""

#a
def volume(lista):
    maxim = lista[0]
    for a in lista:
        if a[-1] > maxim[-1]:
            maxim = a
    return maxim[
"""
Definimos primeiro o valor maximo como sendo o volume da primeira empresa
posiçao 0 e o valor do volume desta que esta na posiçao 6. depois
percorre se o resto das empresas e se esse valor for maior entao passa a ser
esse o maior
"""

#b
def data(lista):
    for a in lista:
        ...
        
"""
Como cada coisa aparece mais do que uma unica vez, o nome então temos 
que comparar com esses dentro da mesma empresa
Com o primeiro for temos a divisão em


"""
#c
def valdaily(lista):
    ...
"""
A empresa com maior valorizaçao diaria sera aquela em que a diferença
do preço de fecho entre dias é a maior
"""

#d
def valgreatest():
    ...
"""
a empresa com maior valorização será aquela em que a variação de preço de
fecho é a maior, sendo esta positiva
"""

#e
def carteira(lista,data1,data2):
	carteira = {}
"""

"""

def main():
    lista_simplificada,lista_dividida = converter()
    volume_maior = volume(lista_simplificada)
    print(volume_maior)
    b = data(lista_dividida)
    
main()
