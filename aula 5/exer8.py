def main():
	total = 0.0
	counter = 1
	
	while True:
		a = input("Introduza um número: ")
		if a == "": break
		s = float(a)
		if counter == 1:
			maxim = s
			minim = s
		if s > maxim:
			maxim = s
		
		if s < minim:
			minim = s
		
		total += s
		w = total/counter
		counter += 1		
		
	print("O valor máximo é de {}, o valor mínimo é de {} e o valor médio é de {}".format( maxim, minim, w))
main()
