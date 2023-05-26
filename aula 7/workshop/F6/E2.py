def readsequence():
	lst = []
	while True:
		x = input("Introduza um numero: ")
		if x == "":
			return lst
		lst.append(float(x))

def countLower(lst,v):
	count=0
	for i in lst:
		if i < v:
			count+=1
	return count

def minmax(lst):
	minn= lst[0]
	maxn= lst[0]
	for i in lst:
		if i > maxn:
			maxn = i
		elif i < minn:
			minn = i
	return minn,maxn

def main():
	# Ler os numeros e guardalos na lista "lst"
	lst = readsequence()

	# Obter a media entre o min e o max
	minn,maxn = minmax(lst)
	media = (minn+maxn)/2

	# Contar os valores mais baixos que a media
	low = countLower(lst,media)

	print("Lista: {}\nmedia: {}\ncontagem: {} ".format(str(lst),media,low))

main()
