
ATP1 = float(input("A nota de ATP1: "))
ATP2 = float(input("A nota de ATP2: "))
AP1 = float(input("A nota de AP1: "))
AP2 = float(input("A nota de AP2: "))
CTP = (ATP1 + ATP2)/2
CP = (AP1 + AP2)/2

if CTP < 6.5 or CP < 6.5:
    NF = "Código 66"
else:
    NF = 0.3*CTP + 0.7*CP
    NF = round(NF)
    
print(NF) 

if NF == "Código 66":
    ATPR = float(input("A nota de ATPR: "))
    APR = float(input("A nota de APR: "))
    NF = 0.3*ATPR + 0.7*APR
    print(round(NF))
