# Complete o programa!

# a)
def loadFile(fname):
	lst = []
	f = open(fname,"r")
	f.readline()
	for line in f:
		numero,nome,curso,regime,datainscricao,nota1,nota2,nota3 = line.split("\t")
		tuplo = (numero,nome,float(nota1),float(nota2),float(nota3))
		lst.append(tuplo)
	f.close()
	return lst

# b)
def notaFinal(reg):
	return (reg[-1]+reg[-2]+reg[-3])/3

# c)
def printPauta(lst):
	print("{:<6} {:^65} {:>4}".format("Numero","Nome","Nota"))
	for e in lst:
		print("{:>6} {:^65} {:>4.1f}".format(e[0],e[1],notaFinal(e)))
	return

# d)
def main():
	# ler o ficheiro
	lst = loadFile("school.csv")
	# ordenar a lista
	lst.sort(key = lambda e : int(e[0]))
	# mostrar a pauta
	printPauta(lst)
# Call main function
main()
