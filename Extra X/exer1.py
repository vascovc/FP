def validate(num):
    if num.isdigit():
        if 3<= len(num)<=9:
            return True
    if num[0] == "+":
        if num[1:].isdigit():
            if 4<=len(num)<=10:
                return True
    return False
"""
Verifica se se o numero e possivel
caso seja todo constituido por digitos ent tem que ter aquele tamanho
caso tenha um mais no inicio ent dali para a frente so pode ser digitos e o tamanho
ja se adiciona 1 ao caso anterior
"""
def call():
    a,b = False,False
    while not a:
        num1 = input("Telefone origem?")
        a = validate(num1)
    while not b:
        num2 = input("Telefonde destino?")
        b = validate(num2)
    dur = input("Duração (s)")
"""
alinea c)
"""
def readfile():
    fich = input("Ficheiro? ")
    #fich = "chamadas1.txt"
    lst = []
    with open(fich) as ficheiro:
        for line in ficheiro:
            origem,destino,duration = line.split()
            tuplo = origem,destino,duration
            lst.append(tuplo)
    #print(lst)
    return lst
"""
abre-se o ficheiro e depois transforma-se para lista
"""

def lstord(lst):
    clientes = []
    for num in lst:
        if num[0] not in clientes:
            clientes.append(num[0])
    #print(sorted(clientes))
    return clientes
"""
Apenas se cria uma lista com os numeros de quem fez a chamada
"""

def fatura(clientes,lista):
    num = input("Cliente? ")
    #num = "960373347"
    if num not in clientes:
        fatura(clientes,lista)
    soma = 0
    print("Fatura do cliente",num)
    print("{:15s} {:7s} {:4s}".format("Destino","Duração","Custo"))
    for a in lista: # metodo nao muito recomendavel mas funciona
        if a[0] == num:
            destino = a[1]
            duracao = int(a[-1])
            custo = 0
            if destino[0] == "2":
                custo = (0.02/60)*duracao
            elif destino[0] == "+":
                custo = (0.80/60)*duracao
            elif destino[0] == num[0] and destino[1] == num[1]:
                custo = (0.04/60)*duracao
            else:
                custo = (0.10/60)*duracao
            soma += custo
            print("{:15s} {:7d} {:4.2f}".format(destino, duracao,custo))
    print("{:15s} {:7s} {:4.2f}".format("","Total:",soma))
"""
Pede-se o numero e podemos verificar se ele faz parte da lista dos clientes, se nao
fizer então pedimos outra vez para inserir o numero
e vai se a lista e se o primeiro numero do tuplo corresponder ao numero do cliente entao
o destinatario vem é o numero a seguir o tuplo e o a seguir a esse a duraçao da chamada
depois temos o custo para a duraçao
"""

def main():
    choice = input("1) Registar chamada\n2) Ler ficheiro\n3) Listar clientes\n4) Fatura\n5) Terminar\nOpção?")
    if choice == "1":
        call() 
        main()
    elif choice == "2":
        lst1 = readfile()
        main()
    elif choice == "3":
        lst1 = readfile()
        clientes = lstord(lst1)
        main()
    elif choice == "4":
        lst1 = readfile()
        clientes = lstord(lst1)
        fatura(clientes,lst1)
        main()
    elif choice == "5":
        quit()
    elif choice == "":
        quit()
    else:
        print("Opçao nao disponivel")
        main()
        
main()
