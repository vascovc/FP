# NMEC: 
# NOME: 

import random

"""
Um vagão é uma lista [mercadoria, quant] com 0<quant<=60 toneladas.
Um comboio é uma lista de vagões.
"""

# Capacidade máxima dos vagões:
Qmax = 60

# Constantes para indexar os vagões.
# Se w==['coal', 45], então w[M]=='coal' e w[Q]==45.
M,Q = 0,1

# Esta função cria um comboio aleatório (NÃO PRECISA PERCEBER).
def randomTrain(a, b=0):
    types = ["coal", "iron", "sand", "salt", "sugar", "rice"]
    n = a if a>b else random.randint(a, b)
    train = []
    for i in range(n):
        wagon = [random.choice(types), random.randint(1, Qmax)]
        train.append(wagon)
    return train

##################################################################################
#Lembrar que existem variaveis universais que evitam usar o 1 e 0 para aceder aos
#valores das listas
##################################################################################

#a)
def quantityOf(t, m):
    """Quantidade total de mercadoria de tipo m no comboio t."""
    soma = 0
    for carruagem in t:
        if carruagem[0] == m:
            soma += carruagem[1]
    return soma
"""
Percorre-se o comboio e se a carruagem for a daquilo que nos queremos
entao devolvemos o valor que la esta
"""
#b)
def unload(t, m, q):
    """Descarrega quantidade q de mercadoria de tipo m."""
    lst = []
    while q > 0 and len(t):
        v = t.pop()
        if v[M] == m:
            v[Q] -= q
            if v[Q] >= 0:
                r = 0
            else:
                q = -1*v[Q]
                v[Q] = 0
                r = q
        lst.append(v)
    while len(lst):
        a = lst.pop()
        if a[Q] !=0:
            t.append(a)
    return r

"""
O mais fácil é primeiro pegarmos numa carruagem e vimos se tem a mercadoria que nos
queremos se nao tiver entao vai logo para a nossa lista auxiliar para depois 
retornarmos ao comboio.
Se tiver aquilo que nos queremos entao vamos lhe tirar a quantidade que queremos.
Se lá ficarmos com uma quantidade maior ou igual a zero entao perfeito ja esta feito
Se a carraugem ficar com um valor negativo entao sabemos que isso nao pode ser e entao
guardamos a quantidade em falta como o simetrico do valor que tem a carruagem e devolvemos
o valor a carruagem de 0 pois n da para ela ter menos que isso.
Existe outra situaçao que e nao chegar mesmo e dai se ter o "r" que vai ser o nosso resto
que depois temos que o devolver

Depois vamos é ter que passar da nossa lista auxiliar para a lista t mas so vamos la colocar
as que tiverem mercadoria superior a 0
"""
#c)
def merchandise(t):
    """Devolve tabela com a quantidade de cada mercadoria no comboio t."""
    dic = {}
    for carruagem in t:
        if carruagem[0] not in dic:
            dic[carruagem[0]] = carruagem[1]
        else:
            dic[carruagem[0]] += carruagem[1] 
    return dic
"""
Vamos percorrer a lista e vemos se a mercadoria ja esta n
"""

#d)
def trainsPerMerchandise(trains):
    dic = {}
    for train_ in trains:
        for a in trains[train_]:
            if a[0] not in dic:
                dic[a[0]] = {train_}
            else:
                set1 = dic[a[0]]
                set2 = {train_}
                dic[a[0]] = set1|set2
    return dic
"""
Vamos percorrendo o dicionario e a cada comboio vemos as carraugens que tem, se a
mercadoria que esta na carruagem nao estiver no nosso dicionario entao acrescentamos e
dizemos que veio desse comboio
Se ja la estiver entao vamos adicionar o nome deste comboio, se for o mesmo, como é um set
e irrelevante que depois apaga
"""

def main():
    random.seed("abc") # Pode alterar o argumento para obter comboios distintos

    t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
    #t = randomTrain(5)  # descomente se quiser gerar outro comboio
    print("t:", t)
    
    print("\na)")
    print(quantityOf(t, 'rice'),
          quantityOf(t, 'iron'),    
          quantityOf(t, 'coal'),    
          quantityOf(t, 'salt'))    

    print("\nb)")
    q = unload(t, 'rice', 40)
    print("unload(t, 'rice', 40) ->", q)
    print("t:", t)
    q =unload(t, 'coal', 50)
    print("unload(t, 'coal', 50) ->", q)
    print("t:", t)
    q =unload(t, 'iron', 20)
    print("unload(t, 'iron', 20) ->", q)
    print("t:", t)

    print("\nc)")
    print(merchandise(t))
    print("t:", t)

    print("\nd)")
    trains = { tid: randomTrain(1,5) for tid in ['T1', 'T2', 'T3', 'T4'] }
    print("trains:", trains)
    trainsPerM = trainsPerMerchandise(trains)
    print(trainsPerM)

main()



