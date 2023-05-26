
# Calcula o factorial de n, baseado na recorrencia n! = n*(n-1)!.
# Mas não termina!  Detete a causa e corrija o erro.
def fact(n):
    if n<=1: # tem que se contar com a convenção de 0! ser igual a 1
        return 1
    else:
        return n*fact(n-1)
"""
Se o valor for 1, que é o ultimo para o calculo ent devolve-se 1 e
vai ser essa nossa base para a regressao chegar ao fim
"""

# Calcula o maximo divisor comum entre a e b.
# Baseia-se no algoritmo de Euclides.
# Mas não termina!  Detete a causa e corrija o erro.
def gcd(a, b):
    if b == 0:
        return a
    else: return gcd(b, a%b)
"""
O algoritmo de euclides funciona usando o resto da divisão como entrada
para o passo seguinte, ou seja o que estava a dividir passa a ser o que é
dividido, sendo dividido pelo resto da divisão anterior
"""


print( fact(4) )    # 24
print( fact(5) )    # 120

x = 2*27*53*61
y = 2*2*17*23*53
print(x, y, gcd(x, y))
assert gcd(x, y) == 2*53

