# coding: utf-8

def tax(r):
	if r<= 1000:
		return 0.1*r
	elif r <= 2000:
		return 0.2*r - 100
	else:
		return 0.3*r - 300

def main():
	print(tax(500))
	print(tax(1500))
	print(tax(2500))
	print(tax(1000))

main()