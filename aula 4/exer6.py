def intersects(a1,b1,a2,b2):
    assert a1<=b1
    assert a2<=b2
    if b1 <= a2 or b2 <= a1:
       return bool("")
    else:
       return bool("a")

a1 = float(input("A1: "))
a2 = float(input("A2: "))
b1 = float(input("B1: "))
b2 = float(input("B2: "))

print(intersects(a1,b1,a2,b2))
