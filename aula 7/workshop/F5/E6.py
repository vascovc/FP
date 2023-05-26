# Complete the code to make the HiLo game...

import random

def main():
	# Pick a random number between 1 and 100, inclusive
	secret = random.randrange(1, 101);
	print("Can you guess my secret?")
	# put your code here
	guess = int(input("Guess: "))
	while guess != secret:
		if guess < secret:
			print("Too Low! Try again.")
		elif guess > secret:
			print("Too High! Try again.")
		guess = int(input("Guess: "))
	print("You Win!")
main()
