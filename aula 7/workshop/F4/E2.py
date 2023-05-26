# coding: utf-8

def p(x):
	return x**2 + 2*x + 3

def main():
	print("p(0)= ",p(0),"\np(1)= ",p(1),"\np(2)= ",p(2),"\np(p(1))= ",p(p(1)))
	return

main()