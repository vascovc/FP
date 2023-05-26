def games():
    lista = []
    jogos = []
    while True:
        x = input("Equipa: ")
        if x == "": break
        lista.append(x)
    
    for i in range(len(lista)):
        for n in range (len(lista)):
            c = lista[i] + ',' + lista[n]
            if i != n: jogos.append(c)
    print(jogos)
games()
