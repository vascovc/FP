def isPalidrome(s):
	for i in range(len(s)):
		if s[i] == s[-1*i-1]: return True
		else: return False


s = input("A palavra a verificar se é palíndromo: ")
print(isPalidrome(s))
