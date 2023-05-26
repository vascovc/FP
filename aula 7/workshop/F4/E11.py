# coding: utf-8

def mdc(a,b):
	r = a%b
	if r == 0:
		return b
	return mdc(b,r)

print(mdc(5,20))
print(mdc(5,30))
print(mdc(20,75))
print(mdc(3,21))