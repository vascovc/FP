def ispalindrome(s):
	for i,a in enumerate(s):
		if a != s[-i-1]:
			return False
	return True

def main():
	print(ispalindrome("ana"))
	print(ispalindrome("bla"))
	print(ispalindrome("abba"))

main()