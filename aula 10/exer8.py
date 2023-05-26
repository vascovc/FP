# COMPLETE a função abaixo.
# Veja os exemplos de utilização e resultados esperados.

# polynomial2(a,b,c) deve devolver uma função f tal que
# f(x) seja o polinómio de segundo grau ax²+bx+c.
def polynomial2(a, b, c):
    return lambda x: a*x**2 + b*x+c

"""
Aqui temos que devolver uma funçao para calcular o valor
entao e so dizermos que o que ela tem que fazer e multiplicar
a por x ao quadrado, b por x e adicionar c
"""
# Testes:
xx = [0, 1, 2, 3]   # Valores de x a testar

p = polynomial2(1, 2, 3)    # creates p(x)=x²+2x+3
print([p(x) for x in xx])   # [3, 6, 11, 18]

q = polynomial2(2, 0, -2)   # creates q(x)=2x²-2
print([q(x) for x in xx])   # [-2, 0, 6, 16]



# DESAFIO EXTRA:
# Crie uma versão generalizada que cria polinómios de qualquer grau.
# (Não é tão fácil com expressões lambda.)

# polynomial(a), onde a=[a0, a1, ..., an], deve devolver uma função f tal que
# f(x) seja o polinómio a0*x**n + a1*x**(n-1) + ... + an.
def polynomial(coefs):
    f = lambda x: 0
    for a in range(len(coefs)):
        f = lambda x,grau = len(coefs)-a-1,coe = coefs[a] ,k=f: k(x) + coe*x**grau
    return f
"""
Começa-se a ver a lista, o primeiro coeficiente e elevado ao maior grau, se a lista tiver 3 valores
entao o primeiro e de grau dois pelo que se tira o "a" e o 1 que da dois,grau = 3-0-1=2 , para a posiçao seguinte, "a"
e igual a 1 e o grau vai ser 3-1-1=1 e assim sucessivamente, e depois colocamos o grau correspondente
relembrando que temos que ir somando com a funcao que fomos criando anteriormenente com o ciclo
"""

# Testes:
r = polynomial([1, 2, 3])   # same as p(x)
print([r(x) for x in xx])   # [3, 6, 11, 18]

s = polynomial([1, -1, 0, 100])     # creates s(x)=x³-x²+100
print([s(x) for x in xx])           # [100, 100, 104, 118]
