def countdigits():
    counter = 0
    palavra = input("o valor: ")
    for i in range(len(palavra)):
        x = palavra[i]
        if x.isdigit(): counter += 1
    print(palavra, "tem",counter, "digitos")

countdigits()
