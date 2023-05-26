def divisors(n):
	lista = [1]
	for i in range(2,n):
		if n%i == 0:
			lista.append(i)
	return lista

def classify(x,lista):
	soma = 0
	for n in lista:
		soma += n
	print(soma)
	if soma > x:
		return "Numero abundante."
	elif soma == x:
		return "Numero perfeito."
	else:
		return "Numero deficiente."

def main():
	x = int(input("Inteiro positivo: "))
	print(divisors(x))
	print(classify(x,divisors(x)))

main()