def Fibonacci(n):
	if n <= 1:
		return n
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci2(n):
	x = 0.0
	a = 0.0
	b = 1
	if n <= 1:
		return n
	else:
		for d in range(2,n):
			x = a + b
			a = b
			b = x
		return x

i = int(input("Qual o termo da sequência de Fibonacci que pretende saber: "))
print(Fibonacci2(i))
print(Fibonacci(i-1))
