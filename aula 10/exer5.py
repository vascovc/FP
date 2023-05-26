#Agradecimento a Tiago Alvim
import bisect
with open("/usr/share/dict/words") as ficheiro: # apenas abre em Linux
    lista = [a.strip() for a in ficheiro]
"""
Assim temos uma lista com todas as palavras e que ja se encontra por
ordem como no ficheiro
"""
def search(lst,x):
    last = x[:-1] + chr(ord(x[-1])+1) # ou entao last = "eb" mas so funciona aqui neste caso
    #print(x)
    #print(last)
    n1 = bisect.bisect_left(lst,x)
    n2 = bisect.bisect_left(lst,last)
    #print(lst[n1])
    
    #print(lst[n2])
    
    return n2-n1

print(search(lista,"ea"))
print(search(lista,"tb")) # aqui já nao se pode usar a simplificaçao para eb pois n faz sentido

"""
começamos por definir o ultimo caracter da string que será entao eb
dizemos que é a string que via ate a penultima letra e depois mudamos
para o ultimo caracter ser entao o seguinte, se era preciso neste 
exercicio pensar ja assim, nao nao era mas assim ficamos ja com um algoritmo para
a proxima alinea
depois temos entao que fazer a nossa procura, aqui o bissect left e mais facil
que indica a posiçao onde o primeiro valor se encontra que e o que se prentende
primeiro encontramos a posiçao do primeiro ea e depois encontramos a posiçao do eb
subtraem-se os indices e obtem se o que se pretende
"""

def search2(lst,x):
    value = search(lst,x) # em vez de modificar a funçao de cima, chama-se esta
    if value == 0:
        x = x[:-1] + chr(ord(x[-1])+1)
        return search2(lst,x)
    else:
        val = bisect.bisect_left(lst,x)
        return lst[val]
"""
Para nao estarmos a escrever tudo outra vez usamos a funcao anterior e vemos quantas
palavras ha com aquele inicio, se for nenhuma entao vemos se ha com a letra a seguir e 
se nao houver voltamos a ver se há com a que vem a seguir, se ja houver entao, como o 
enunciado pede vemos qual e que e a primeira palavra e devolvemos essa palavra
"""
print(search2(lista,"tb"))
