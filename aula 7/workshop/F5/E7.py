def leibnizPi4(n):
	if n == 0:
		return 1
	return ((-1)**n)/((2*n)+1) + leibnizPi4(n-1)


def main():
	print(leibnizPi4(950)*4)

main()