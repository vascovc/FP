def abrevi(name):
	x = ""
	for i in range(len(name)):
		if name[i].isupper(): x += name[i]
	return x
	
name = input("nome: ")	
print(abrevi(name))
