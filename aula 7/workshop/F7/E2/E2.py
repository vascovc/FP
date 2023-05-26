# Exercise 5 on "How to think...", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
filepath = "mystery.txt"
f = open(filepath,"r")
for line in f:
	if line.strip() == "UP":
		t.up()
	elif line.strip() == "DOWN":
		t.down()
	else:
		print(line)
		x,y = line.split(" ")
		t.goto(float(x),float(y))

f.close()


# wait 
turtle.Screen().exitonclick()
