# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    c = 0
    a = "something"
    while  a != "You are right":
        i = int(input("The number you think it is: "))
        if i < secret:
            a = "Low"
        elif i == secret:
            a = "You are right"
        else:
            a = "High"
        print(a)
        c += 1
    print("It took you",c,"tries")
    
  


main()
