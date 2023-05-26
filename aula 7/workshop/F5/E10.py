def isPrime(n):
	if n == 1:
		return False
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def main():
	for n in range(1,101):
		print("{:3d} {:5s}".format(n,str(isPrime(n))))

main()