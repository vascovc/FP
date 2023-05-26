import math
def zerodown(x1,x2,precision,f):
    assert x2 > x1
    x3 = x1
    while (x2-x1) >= precision:
        x3 = (x1+x2)/2
        if f(x3) == 0:
            return x3
        if f(x3)*f(x1) < 0:
            x2 = x3
        else:
            x1 = x3
    return x3
"""
Entao enquanto o intervalo que vamos estar a reduzir for maior
que a precisao que necessitamos. Criamos o ponto a meio dos
extremos. se o f desse valor for 0 ja ganhamos, se nao for
entao temos que fazer outras coisas. se o ponto menor do extremo
e o nosso x3, os f destes, for menor que zero entao quer dizer
que tem sinais contrarios pelo que podemos encortar o intervalo
pondo o nosso x2= x3. se o resultado for maior que 0 entao quer dizer
que tem o mesmo sinal pelo que o nosso extremo inferior passa a ser
o tal ponto medio
aqui o objetivo e ir sempre diminuindo o intervalo de forma a termos
um valor muito proximo
"""

f = lambda x: x+math.sin(10*x)
a = zerodown(0.2,0.4,0.0001,f)
b = zerodown(0.4,0.6,0.0001,f)
print(a)
print(b)
