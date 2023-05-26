def mediana(lst):
    lista = sorted(lst)
    if len(lista)%2 == 0:
        med1 = lista[int(len(lista)/2 -1)]
        med2 = lista[int(len(lista)/2)]
        med = (med1+med2)/2
    else:
        med = lista[int(len(lista)//2)]
    return med

print(mediana([1,0,2,3,5]))
print(mediana(range(1,20)))

"""
Primeiro ordena-se a lista que é mais fácil e depois vemos
se o comprimento dela é par ou impar e se for impar faz-se a
media dos elementos centrais se for impar é so ir buscar esse
numero
"""
