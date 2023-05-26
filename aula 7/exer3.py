
# Agradecimento especial ao Hugo que sem ele a resoluç\ao deste exercicio seria impossível


# a)
def loadFile(fname):
    lst = []
    with open(fname, "r") as ficheiro:
        ficheiro.readline()
        for line in ficheiro:
            numero,nome,curso,regime,datainscricao,nota1,nota2,nota3 = line.split("\t")
            tuplo = (numero,nome,float(nota1),float(nota2),float(nota3))
            lst.append(tuplo)
    return lst
""" 
lê a primeira linha que no ficheiro tem os cabeçalhos e cria um tuplo com as coisas que
queremos e faz a divisão nos tab que era o que dizia no enunciado pelo que estava separado

"""
# b)
def notaFinal(reg):
    nota = (reg[-1]+reg[-2]+reg[-3])/3
    return nota
"""
Só os ultimos tres itens da lista e que interessam que são as notas dos alunos
então vamos ao contrário à lista buscar os valores porque n\ao sabemos nem queremos
saber quantos itens da lista
"""


# c)
def printPauta(lst):
    print("{:<6} {:^65} {:>4}".format("Numero","Nome","Nota"))
    for e in lst:
        print("{:>6} {:^65} {:>4.1f}".format(e[0],e[1],notaFinal(e)))
"""
vai a cada linha e imprime, aqueles caracteres tem que ser mesmo assim para ficar
bonito. e depois é entao o numero que na lista e a posiçao 0 o nome p1 e depois a
nota que se chama com a função
"""

#4
def printPautaficheiro(lst,ficheiro):
    print("{:<6} {:^65} {:>4}".format("Numero","Nome","Nota"), file = ficheiro)
    for e in lst:
        print("{:>6} {:^65} {:>4.1f}".format(e[0],e[1],notaFinal(e)), file =ficheiro)
"""
Este coiso é igual ao imprimir anterioe só que imprime para um ficheiro
"""
def main():
    # ler o ficheiro
    lst = loadFile("school.csv")
    # ordenar a lista
    lst.sort(key = lambda e : int(e[0])) # a função lambda é algo curioso mas assim dá meter por ordem crescente
    # mostrar a pauta
    printPauta(lst)
#4    
    with open("exe_4.txt","w") as ficheiro:
        printPautaficheiro(lst,ficheiro)

# Call main function
main()

