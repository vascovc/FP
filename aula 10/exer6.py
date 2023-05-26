import bisect
with open("/usr/share/dict/words") as ficheiro: # apenas abre em Linux
    lista = [a.strip() for a in ficheiro]

lista_1 = []
while True:
    word = input("Palavra: ")
    if word == "":
        break
    last = word[:-1] + chr(ord(word[-1])+1)
    n1 = bisect.bisect_left(lista,word)
    n2 = bisect.bisect_left(lista,last)
    for a in range(n1,n2):
        lista_1.append(lista[a])
    if len(lista_1) == 0:
        print("No words found")
    else:
        print(lista_1)
    lista_1 = []
    
"""
Muito semelhante ao exercicio 5 mas temos que ter atencao que se coloca num ciclo
"""
