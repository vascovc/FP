liters = float(input("The number of liters: "))
price = liters * 1.40
if liters > 40:
    price = price*0.90
print("The price to pay is",price)
