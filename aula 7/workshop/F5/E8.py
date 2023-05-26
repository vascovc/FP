get = int(input("Primeiro Numero: "))
maxn = get
minn = get
it = 0
media = get
while True:
	it += 1
	get = input("Proximo numero: ")
	if get == "":
		break
	get = int(get)
	if get > maxn:
		maxn = get
	elif get < minn:
		minn = get
	media = (it*media + get)/(it+1)

print(maxn,minn,media)