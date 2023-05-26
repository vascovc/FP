# This program outputs the age category for a given input age.
# It has a semantic error.  Can you find it?
# Which values of age produce the output "adult"?
# Correct the error.
# Can you simplify the code to avoid redundant conditions

age = int(input("Age? "))

if age <= 12 :
    cat = "child"
elif age < 20:
    cat = "teenager"
else:
    cat = "adult"

print("Category:", cat)

