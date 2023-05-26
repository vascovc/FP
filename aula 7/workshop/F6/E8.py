def evenThenOdd(s):
	odd = s[1::2]
	even = s[::2]
	return even + odd

def removeAdjacentDuplicates(s):
	last = ""
	new_s= ""
	for l in s:
		if l != last:
			new_s+= l
		last = l
	return new_s

def reapeatNumTimes(n):
	lst=[]
	for i in range(1,n+1):
		for j in range(1,i+1):
			lst.append(i)
	return lst

def positionOfFirstLargest(arr):
	max_index=0
	max_num=arr[0]
	for i,n in enumerate(arr):
		if n > max_num:
			max_num = n
			max_index = i
	return max_index

def main():
	print(evenThenOdd("abcd"))
	print(removeAdjacentDuplicates("Mississipi"))
	print(reapeatNumTimes(7))
	print(positionOfFirstLargest([1,2,3,4,5,6,1]))

main()