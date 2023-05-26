def factorial(n):
	x = 1
	while n > 0:
		x *= n
		n -= 1
	return x
		
i = int(input("Um número: "))
print(i,"! = ",factorial(i))
