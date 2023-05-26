# Resolucao recursiva sem listas

def fibo(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	return fibo(n-1) + fibo(n-2)


# Resolucao com listas
def fibolist(n):
	lista = [0,1]
	for i in range(2,n):
		lista.append(lista[i-1]+lista[i-2])
	return lista[-1]

def main():
	print(fibo(5))
	print(fibo(6))
	print(fibo(7))
	print(fibo(8))
	print(fibolist(9))
	print(fibolist(10))
main()
