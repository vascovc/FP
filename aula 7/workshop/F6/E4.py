def allMatches(lst):
	final_lst=[]
	for i in lst:
		for j in lst:
			if i != j:
				final_lst.append((i,j))
	return final_lst

def main():
	equipas = ['FCP','SCP','SLB','RAV']
	print(allMatches(equipas))
	print(len(allMatches(equipas)))

main()