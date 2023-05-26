def val(jor):
    with open("Jornadas.csv") as ficheiro:
        lst =[]
        for line in ficheiro:
            lst.append(line.strip("\n").split(","))
        for jornada in lst:
            if jor == jornada[0]:
                return True,lst
        else:
            return False,lst
def main():
    jornada = input("Jornada? ")
    a,b = val(jornada)
    if not a:
        print("Jornada inválida")
        main()
    count = 0
    aposta = []
    for game in b:
        if game[0] == jornada:
            count += 1
            result = input(("{} {} vs {}: ".format(game[0],game[1],game[2])))
            while True:
                if result == "X" or result == "1" or result =="2":
                    break
                else:    
                    print("Aposta invalida")
                    result = input(("{} {} vs {}: ".format(game[0],game[1],game[2])))
            aposta.append((count,int(result)))
    name = "jornada" + jornada + ".csv"
    with open(name,"w") as escrita:
        for a in aposta:
            print(a, file = escrita)
    
    #b)
       
main()
