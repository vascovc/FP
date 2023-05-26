def isPrime(n):
	x = 1
	z = 0
	while n % x == 0:
		x += 1
	if x <= 2: z = bool("yte")
	else: z = bool("")
	if n == 1: z = bool("")
	if n == 2: z = bool("yey")
	return z 

i = int(input("Introduza um número para verificar se é primo: "))
print(isPrime(i))

for a in range(1,101):
	print(a)
	print(isPrime(a))
