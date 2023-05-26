# This function sorts a list (like list.sort)
# using the insertion sort algorithm.
# Modify it to accept a key= keyword argument that works like in list.sort.

def insertionSort(lst, key = None):
    i = 1  # i = index of element to insert next = end of sorted part
    if key != None:
        while i < len(lst):
            x = lst[i]    # x is the element to insert
            # insert x into lst[:i]
            k = i-1
            while k >= 0 and key(lst[k]) > key(x):#####
                lst[k+1] = lst[k]
                k -= 1
            lst[k+1] = x
            i += 1
    else:
        while i < len(lst):
            x = lst[i]    # x is the element to insert
            # insert x into lst[:i]
            k = i-1
            while k >= 0 and lst[k] > x:
                lst[k+1] = lst[k]
                k -= 1
            lst[k+1] = x
            i += 1
"""
A alteraçao que se tem que fazer e tornar a funçao a aceitar mais 
um parametro e se esse parametro for alguma coisa entao nao vamos
comparar com a lista em si mas com o valor que a chave da a esse item
da lista.
se for entao a funcao mantem se igual
"""

# Original list
lst0 = ["paulo", "augusto", "maria", "paula", "bernardo", "tito"]
print("lst0", lst0)

# sort in lexicographic order:
lst = lst0.copy()
insertionSort(lst)
print("lst1", lst)
assert lst == sorted(lst0)

# sort by length (requires key= argument):
lst = lst0.copy()
insertionSort(lst, key=len)
print("lst2", lst)
assert lst == sorted(lst0, key=len)

# sort by length, than lexicographic order:
myorder = lambda s:(len(s), s)
lst = lst0.copy()
insertionSort(lst, key=myorder)
print("lst3", lst)
assert lst == sorted(lst0, key=myorder)

print("All tests OK!")
