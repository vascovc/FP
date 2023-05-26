def countDigits(string):
	counter = 0
	for a in string:
		if a.isdigit():
			counter += 1
	return counter

def main():
	print(countDigits("123456"))
	print(countDigits("bla"))
	print(countDigits("123blabla45"))

main()