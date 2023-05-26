
# Add functions here
def printTable(people):
    print("{:<10s}{:>10s}{:>10s}{:>10s}".format("Nome","Peso","Altura","IMC"))
    for name in people:
        imcs = imc(name)
        print("{:<10s}{:>10.1f}{:>10.2f}{:>10.1f}".format(name[0],name[1],name[2],imcs))
"""
a unica coisa chata aqui são as formataçoes, o caracter < indica que é colocado
a esquerda o valor e > que é à direita, os numeros indicam o espaçamento, neste 
caso escolhi o 10 quando se coloca o ponto o valor que vem a seguir diz quantas
casas decimais são e a letra a seguir é a indicar o tipo s-string f-float
"""

def imc(name):
    result = name[1]/name[2]**2
    return result
"""Apenas calcula o imc e devolve o valor"""
def inputBetween(frase,minimo,maximo):
    while True:
        valor = float(input(frase))
        if minimo <= valor <= maximo:
            break
        else: print("Value out of range")
    return valor
"""
Esta funçao pede entao o valor ao utilizador e se esse valor
estiver dentro daquee intervalo entao aceita-o caso contrario 
vai continuar a pedir valores
"""
def selectTaller(pessoas,limit):
    lst = []
    for p in pessoas:
        if limit < p[2]:
            lst.append(p)
    return lst
"""
vamos a ver se cada uma dessas pessoas tem altura superior
a que o limite permite, se forem entao adicionamos à lista
o tuplo dos dados
"""

def main():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    # Imprime os dados numa tabela com 4 colunas: nome, peso, altura e IMC.
    printTable(people)
    
    # Pede e devolve um valor, mas só aceita se estiver no intervalo certo.
    limit = inputBetween("altura minima? ", 1.1, 2.5)
    
    # Extrai uma lista de pessoas com altura superior a limit.
    tallpeople = selectTaller(people, limit)
    
    # Mostra uma tabela só com as pessoas altas.
    printTable(tallpeople)


# O programa começa aqui
main()

