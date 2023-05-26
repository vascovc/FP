def tax(r):
    if r <= 1000:
        r = 0.1*r
    elif r <= 2000:
        r = 0.2*r - 100
    else:
        r = 0.3*r - 300
    return r
r = float(input("Tax: "))
print(tax(r))

