lst = [5,3,8,7]
print(len(lst))
print(lst[2])
#print(lst[4])  fora do alcance
print(lst[-4])
print(lst[1:3])
print(lst[:-1])
print(lst[2:2])
lst[2:2] = [99]
print(lst)
t = ("ana", (1974,4,25))
print(len(t))
print(t[1])
print(t[1][0])
print((1974,3,30) < (1974,4,1))
print((1974,3) < (1974,3,-1,-2))
s = "abcde"
print(s[2:] + s[:2])
print(s[1::2])
print(s > "abel")
