#def countdown(n):
 #   n -= 1
  #  print(n)
   # if n > 0:
    #    return countdown(n)
    #if n == 0:
     #   exit()
def countdown2(n):
	if n>0:
		print(n)
		countdown2(n-1)
print("Este programa faz a contagem decrescente a partir de um valor")
n = int(input("Introduza o número para começar: "))

#print(n)
#print(countdown2(n))
countdown2(n)
