def listan():
	lista = []
	while True:
		a = input("Introduza um número para adicionar à lista: ")
		if a == "": break
		b = float(a)
		lista.append(b)
	print(lista)
	return lista
		
def countLower(lst, v):
	n = 0
	x = []
	for i in range(len(lst)):
		if v > lst[i]:
			x.append(lst[i])
			n += 1
	print(n,"é o número de elementos inferiores a",v)
	print("A lista de valores inferiores a",v, "é",x)
	
def minmax(lst):
	x = 0
	maxim = lst[0]
	minim = lst[0]
	for i in range(len(lst)):
		if lst[i] > maxim:
			maxim = lst[i]
		if lst[i] < minim:
			minim = lst[i]
	print("O valor máximo da lista é",maxim)
	print("O valor minimo da lista é",minim)
	return [maxim, minim]

def main():
	lst = listan()
	cd = minmax(lst)
	maximo = cd[0]
	minimo = cd[1]
	media = (maximo+minimo)/2
	countLower(lst,media)		
		
"""lst = listan()
x = float(input("O numero que é máximo que pretende ver: "))
countLower(lst, x)
minmax(lst)"""
main()


		
