# coding: utf-8

def intersects(a1,a2,b1,b2):
	if a1 < b2 and b1 < a2 or a1 > b2 and b1 > a2:
		return False
	return True

def main():
	print(intersects(1,5,3,6)) #Deve devolver False  -> [1,3[ [5,6[
	print(intersects(1,2,3,6)) #Deve devolver True   -> [1,3[ [2,6[

main()