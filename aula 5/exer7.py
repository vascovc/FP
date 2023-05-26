def leibnizPi4(a):
	total = 0.0
	while a >= 0:
		total = ((-1)**a)/(2*a+1) + total
		a -= 1
	return total

a = int(input("Numero de termos para a soma: "))
print(leibnizPi4(a))
