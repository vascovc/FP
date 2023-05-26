# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))
#d
def filterPartName(contactos):
    nome = input("Nome/Parte do nome:")
    dic = {}
    for info in contactos:
        if nome in contactos[info]:
            dic[info] = contactos[info]
    return dic
            
"""
Pede uma string e depois definimos um dicionario para meter para la.
Vamos a percorrer o dicionario e caso alguma da informaçao seja aquela
que corresponde, vemos se a nossa palavra de input esta dentro da que
esta nos contactos e caso esteja entao adicionamos essa informaçao ao
dicionario antes criado
"""

#a 
def addcontact(contactos):
    numero = input("Numero:")
    nome = input("Nome:")
    contactos[numero] = nome
    return contactos
"""    
Pede o numero e o nome e adiciona ao dicionario
"""

#b
def removecontacts(contactos):
    numero = input("Numero a remover:")
    del contactos[numero]
    return contactos
"""
Pede o numero e apaga esse numero e nome da lista
"""

#c
def searchnumb(contactos):
    numero = input("Numero:" )
    if numero in contactos:
        return contactos[numero]
    else:
        return numero
"""
Pede um numero e ve se este esta na lista se estiver ent devolve o nome
associado caso nao esteja entao devolve o proprio numero
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
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
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


