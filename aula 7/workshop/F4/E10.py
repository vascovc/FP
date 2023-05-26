# coding: utf-8

def countdown(N):
	if N < 0 : # condicao 1
		return
	print(N)
	if N == 1:
		return
	countdown(N-1)
	return

countdown(10)
countdown(-1) # Dá erro sem a condicao 1
countdown(15)