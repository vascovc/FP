# This program should find the phase of a fictional substance
# for given temperature and pressure conditions, but it has several bugs!
# 
# a) Try to run the program with Python3 and see what happens.
#    There's a syntax error near the end.  Fix it.
# b) Try again.  It'll crash with a runtime error.  Find the cause and fix it.
# c) There is also a semantic error: for T=300 and P=100, phase should be SOLID.
#    Fix it to agree with the phase diagram.  Test in several conditions!
# d) Adjust the format string to output temperature with 1 decimal place
#    and pressure with 3. 

print("Kryptonite phase classifier")

T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

if P > 50.0:
    if T < 400:
        phase = "SOLID"
    else:
        phase = "LIQUID"
if P < (1/8)*T:
    phase = "GAS"
else:
    phase = "SOLID"
if P == (1/8)*T or (T == 400 and P > 50) or (T > 400 and P == 50):
    print("At {}K and {}kPa, Kryptoniyte existes in more than one phase.".format(T, P))
    exit()

T = "{:.1f}".format(T)
P = "{:.3f}".format(P)
print("At {}K and {}kPa, Kryptoniyte is in the {} phase.".format(T, P, phase))
