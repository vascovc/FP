d = {'abc' : 1, 'xyz' : 4, 'klm' : 7}
l = [1, 2, 3, 4, 5]
x = len(d) + len(l)
print(x)
print(d['xyz'])
print(l[4])
k = 0
for x in d:
    k += d[x]
for x in l:
    k += x
print(k)
	
