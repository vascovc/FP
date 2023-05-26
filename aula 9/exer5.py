
def main():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    print("a) Table of common interests:")
    commoninterests = {(a,b): interests[a].intersection(interests[b]) for a in interests for b in interests if b > a}
    print(commoninterests)
    """
    Vamos percorrendo a lista dos nomes e criam-se os pares, a questão do maior não tenho bem a certeza se está correto
    mas não dá os repetidos pelo que foi o que escolhi
    Depois fazemos a interseçao do set dos seus gostos.
    """

    print("b) Maximum number of common interests:")
    maxCI = max([len(commoninterests[(a,b)]) for (a,b) in commoninterests])
    print(maxCI)
    """
    temos o dicionário criado anteriormente e temos que ver qual dos sets de valores é o maior
    cria-se uma lista com o tamanho do numero de elementos, que são os comuns e depois aplica-se 
    a função max que devolve o maior valor.
    Pela figura da alinea d é que digo que o objetivo era ess
    """

    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [(a,b) for (a,b) in commoninterests if len(commoninterests[a,b]) == maxCI]
    print(maxmatches)
    """
    Quere-se entao uma lista dos pares de nomes em que o numero de elementos comuns é igual ao número maximo
    isso nos vimos na alinea anterior pelo que so vamos incluir esse par na lista se o numero de elementos iguais
    for o mesmo
    """

    print("d) Pairs with low simmilarity:")
    lowJaccard = [(a,b) for (a,b) in commoninterests if len(commoninterests[a,b])/len(interests[a].union(interests[b]))<0.25]
    print(lowJaccard)
    """
    Então aqui queremos uma lista com o par de pessoas em que o indice que eles dizzem tem que ser inferior 
    a 25% ou seja o tamanho da intereseçao/tamanho da reunião tem que ser < 0.25
    """


# Start program:
main()

