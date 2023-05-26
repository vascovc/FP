def max2(n1,n2):
	maxim = n1
	if n2 > maxim:
		maxim = n2
	return maxim
	
def max3(x,n3):
	n1 = x
	n2 = n3
	maxim = max2(n1,n2)
	return maxim

n1 = float(input("Um número: "))
n2 = float(input("Um número: "))
n3 = float(input("Um número: "))

x = max2(n1,n2)
y = max3(x,n3)

print("O maior valor da função 1 é ",x)
print("O maior valor da função 2 é ",y)
