# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json

# Abre o ficheiro e descodifica-o criando o objeto twits.
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)

# Analise os resultados impressos para perceber a estrutura dos dados.
print(type(twits))       # deve indicar que é uma lista!
print(type(twits[0]))    # cada elemento da lista é um dicionário.
print(twits[0].keys())   # mostra as chaves no primeiro elemento.

# Cada elemento contém uma mensagem associada à chave "text":
print(twits[0]["text"])

# Algumas mensagens contêm hashtags:
print(twits[880]["text"])


palavras = [ word for a in range(len(twits)) for word in twits[a]["text"].split()]

"""
alinea a
temos assim todas as palavras do ficehiro como sendo elementos de uma lista
"""
def num_times(lst):
    dic = {}
    for a in lst:
        if a in dic:
            value = dic[a]
            value += 1
            dic[a] = value
        else:
            dic[a] = 1
    return dic

numero_vezes = num_times(palavras)
#print(numero_vezes)
"""
Perfeita noçao que nao era este assim o objetivo mas assim ja temos a quantidade
de vezes que cada palavra aparece e a seguir ja se resolve a alinea b, nao se 
infrigiu nada do exercicio tanto quanto leio
"""
def makelist(dic):
    lista = []
    for a in numero_vezes:
        lista.append([a,dic[a]])
    return lista
lista = makelist(numero_vezes)
#print(lista)

def order(lst):
    i = 1   # i = index of element to insert next = end of sorted part
    while i < len(lst):
        x = lst[i]    # x is the element to insert
        # insert x into lst[:i]
        k = i-1
        while k >= 0 and lst[k][1] > x[1]:
            lst[k+1] = lst[k]
            k -= 1
        lst[k+1] = x
        i += 1
    return lst
listar = order(lista)
assert listar == sorted(lista,key = lambda i:i[1]) # nao e preciso mas num teste o professor ficava todo feliz
#print(listar)
"""
Assim ordenamos a lista atraves do algoritmo da aula 10 modificando que
temos que aceder ao valor que corresponde ao numero de vezes que a palavra
aparece
"""

def hash(lst):
    lista = []
    for a in range(len(lst)-1,-1,-1):
        obj = lst[a]
        if obj[0][0]=="#":
            lista.append(obj)
    return lista

hashtag = hash(listar)
#print(hashtag)

"""
por causa da alinea que vem a seguir o melhor e pormos a lista ja ao contrario
e assim vemos se a string associada a cada sublista e inicializada por um "#" e
se for adiciona-se a uma lista
nao e explicito qual a ordem desta lista sendo melhor em avaliacao perguntar qual a
ordem pois tanto faz fazer aqui como em baixo
"""

def printer(lst):
    i = 0
    while i < len(lst):
        obj = lst[i]
        name = obj[0]
        num = obj[1]
        if i == 0:
            greatest = num
        percent = num / greatest * 100
        percentil = (percent / 100) * 18
        percentil = int(percentil)
        hashes = "+" * percentil
        print("{:30s} ,"("{:4.0f},")", {:18s}".format(name,percent,hashes))
        i += 1

printer(hashtag)
"""
Entao vamos utilizar um ciclo. como esta ordenada entao o primeiro numero
de ocorrencias e o maior e corresponde a 100% pelo que depois tem que se fazer
a conta da fracao e multiplicar pelo numero de sinais que tem que aparecer pois
100 % correspondem a 18 sinais e depois e proporcional
"""
