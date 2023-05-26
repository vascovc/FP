# coding: utf-8

def max2(x,y):
	if x > y:
		return x
	else:
		return y

def max3(x,y,z):
	return max2(max2(x,y),z)

def main():
	print(max2(5,6))
	print(max3(1,2,3))

main()