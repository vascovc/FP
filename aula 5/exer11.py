def divisores(n):
	x = 1
	i = 0
	while True:
		if n == x:
			break
		if n % x == 0:
			print(x, "é divisor natural de",n)
			i += x
		x += 1
		
	if i < n: z = "Número deficiente"
	elif i == n: z = "Número perfeito"
	else: z = "Número abundante"
	return z


i = int(input("Um número para verificar os divisores: "))
print(divisores(i))
