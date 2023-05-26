import math
def floatInput():
    try:
        a = input("val?")
        a = float(a)
    except:
        print("Not possible to convert")
        floatInput()
    return a
"""
Tenta um valor introduzido pelo utilizador e caso n seja possível diz erro e
chama a funç\ao outra vez, problema é que ao fim de muitas muitas tentativas
enche a memoria pelo que um ciclo while se pode tornar preferivel nesse
aspeto
"""
def floatInputmaxmin(minim,maxim):
    a = floatInput()
    if a >= float(minim) and a <= float(maxim):
        print("Value in range")
    else:
        print("Value should be in [",minim,"],[",maxim,"]")
        floatInputmaxmin(minim,maxim)
"""
Chama a outra funç\ao para pedir o valor ao utilizador e converter para float
depois ve se esta ou nao dentro do intervalo e se estiver acabou se não pede outra vez
"""
def floatInputOptional(minim = -math.inf,maxim = math.inf):
    if minim != -math.inf and maxim != math.inf:
        a = floatInputmaxmin(minim,maxim)
    else:
        a = floatInput()
    return a
"""
Lá em cima estamos a dar valores default que são os infinitos pelo que assim se o
utilizador colocar lá parametros ele vai tomar esses parametros se n\ao colocar 
entao vai chamar a outra função
"""
#floatInput
#floatInputmaxmin(5,6)
#floatInputOptional()
