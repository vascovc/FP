def arranjos(n,k):
    if k == 0:
        return 1
    else:
        a = arranjos(n-1,k-1)
        return a*n
"""
Analisando a funçao que e dada conseguimos concluir que é
isto que se tem que escrever
"""
print(arranjos(2,1))
print(arranjos(5,2))
print(arranjos(5,3))
print(arranjos(10,3))
