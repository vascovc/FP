
# Devolve o IMC para uma pessoa com peso w e altura h.
def imc(w, h):
    return w/h**2

def main():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    print("People:", people)

    # Esta comprehension define uma lista dos nomes das pessoas em people
    names = [n for n,w,h in people]
        # = [p[0] for p in people]  # equivalente
    print("Names:", names)
    
    # Usando list comprehensions, obtenha: 
    # a) Uma lista com os valores de imc de todas as pessoas.
    imcs = [imc(a[1],a[2]) for a in people]
    print("IMCs:", imcs)
    """
    Para cada pessoa da lista aplica a função imc com os parametros do peso e da altura
    e imprime essa lista gerada
    """

    # b) Uma lista dos tuplos de pessoas com altura superior a 1.7m.
    tallpeople = [ a for a in people if a[2] > 1.7]
    print("Tall people:", tallpeople) 
    """
    a variavel vai guardar a lista com os nomes se o valor para essa altura for superior
    a 1.7metros
    """   

    # c) Uma lista de nomes das pessoas com IMC entre 18 e 25.
    midimc = [names[a] for a in range(len(imcs)) if 18<imcs[a]<25]
    print("Mid-IMC:", midimc)
    """
    vai buscar à lista dos nomes aquelas que tiverem um imc compreendido entre aqueles
    valores. Vamos com o rnage que é para podermos aceder ao valor de imc mais facilmente
    """

# O programa começa aqui
main()

