import math

a = float(input("O comprimento do cateto A: "))
b = float(input("O comprimento do cateto B: "))
c = (a**2 + b**2)**(1/2)
print("A hipotenusa tem o comprimento de: ",c)
ang = b/a
angr = math.atan(b/a)
angd = math.degrees(angr)
print("O ângulo entre o cateto A e a hipotenusa é de: ",angd,"graus")
