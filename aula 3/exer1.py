# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with conditional statements (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))

# Use conditional statements instead of max function!
if x1<x2:
    mx = x2
elif x1==x2:
    print("The values are the same")
else:
    mx = x1
    
print("Maximum:", mx)
