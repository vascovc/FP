def shorten(big):
	small=""
	for l in big:
		if l.isupper():
			small+=l
	return small

def main():
	print(shorten("Universidade de Aveiro"))

main()