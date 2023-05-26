seconds = float(input("O tempo em segundos: "))

hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
s = rest % 60
print(hours,":",minutes,":",s)
