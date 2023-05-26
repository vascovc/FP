# Complete este programa como pedido no guião da aula.
"""
Este progama e copia do do exercicio 3 mas com as alteraçoes necessarias
"""
def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {} : {:<12s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {} : {:<12s}".format(num, dic[num[0]], dic[num[1]]))
"""
Aqui altera-se para dar mais uma coluna ajustada a esquerda < e alteramos para
se ir buscar cada um dos valores
"""        

#d
def filterPartName(contactos):
    nome = input("Nome/Parte do nome:")
    dic = {}
    for info in contactos:
        if nome in contactos[info[1]]:
            dic[info] = contactos[info]
    return dic
"""
Aqui so faz sentido ele ver se o nome esta na posiçao do nome na lista
mas tambem se pode criar uma funçao para verificar parte da morada e mostrar.
como aqui faz mas sem ser com nome ser com morada
"""
#a 
def addcontact(contactos):
    numero = input("Numero:")
    nome = input("Nome:")
    morada = input("Morada:")
    contactos[numero] = nome,morada
    return contactos
"""
Temos que pedir mais a morada
"""

#b
def removecontacts(contactos):
    numero = input("Numero a remover:")
    del contactos[numero]
    return contactos
"""
Mesma coisa do anterior
"""

#c
def searchnumb(contactos):
    numero = input("Numero:" )
    if numero in contactos:
        return contactos[numero]
    else:
        return numero
"""
Mesma coisa do anterior
"""

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ["Universidade de Aveiro","Santiago,Aveiro"],
        "727392822": ["Cristiano Aveiro","Aveiro"],
        "387719992": "Maria Matos",
        "887555987": ["Marta Maia","Coimbra"],
        "876111333": ["Carlos Martins","Porto"],
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addcontact(contactos)
        elif op == "R":
            removecontacts(contactos)
        elif op == "N":
            print(searchnumb(contactos))
        elif op == "P":
            print(filterPartName(contactos))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()


