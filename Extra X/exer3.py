def data():
    with open("hipermercado.txt") as ficheiro:
        lst = []
        for line in ficheiro:
            linha = line.strip()
            lst.append(linha.split(";"))
    print(lst)
    return lst
        
def ins(lst):
    while True:
        co = input("Código: ")
        if co != "0":
            for a in lst:
                if a[0] == co:
                    iva = 0
                    for val in a[4]:
                        if val.isdigit():
                            iva += str(val)
                    print(a[1],":", float(a[3])*(1+0.01*iva),"€")
                else:
                    print("Wrong Code")
        else: break

def sair():
    with open("StockOut.txt","w") as fich:
        ...

def main():
    print("(I)nserir itens")
    print("(F)aturar")
    print("(S)air")
    opt = input("Opção? ")
    lst = data()
    if opt == "I":
        ins(lst)
        main()
    elif opt == "F":
        fat(lst)
        main()
    elif opt == "S":
        sair()
    else:
        print("Option not available")
        main()
main()
