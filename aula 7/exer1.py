def soma():
    nomeficheiro = input("O nome do ficheiro para realizar a soma: ")
    with open(nomeficheiro, "r") as ficheiro:
        soma = 0
        for a in ficheiro:
            try:
                a = float(a)
                soma += a
            except:
                print("Conteudo do ficheiro invalido")
        print(soma)
try:
    soma()
except:
    print("Nome do ficheiro inválido")
    soma()
    
