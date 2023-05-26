def poli(x):
    result = x**2 +2*x + 3
    return result

for x in range (3):
    print(poli(x))
    
print(poli(poli(1)))
