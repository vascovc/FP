# This program uses the module turtle to draw "turtle graphics"
# For an introduction and examples, read
# https://runestone.academy/runestone/static/thinkcspy/PythonTurtle/toctree.html

import turtle               # allows us to use the turtles library

# Make turtle t draw a square with the given side length
def square(t, side):
    for n in range(4):
        t.forward(side)
        t.left(90)

# Make turtle t draw a spiral
def spiral(t, start, end, incr):
    # Complete the function...
    for m in range(start,end+1,incr):
        t.left(90)
        t.forward(m)
    return

def main():
    print("This program opens a window with a graphical user interface.")
    wn = turtle.Screen()        # creates a graphics window
    alex = turtle.Turtle()      # create a turtle named alex

    alex.forward(150)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
    alex.forward(75)            # complete the second side

    beth = turtle.Turtle()      # another turtle
    beth.shape("turtle")        # with another shape
    beth.color("blue")          # and color
    beth.up()                   # pen up
    beth.goto(-200, 0)          # move to given point
    beth.down()                 # pen down
    square(beth, 100)           # draw a square

    # Move alex to another place
    alex.up()
    alex.goto(-200, -200)
    alex.setheading(0)
    alex.down()
    # This should draw a spiral
    spiral(alex, 10, 200, 10)
    alex.up()
    alex.goto(200,-250)
    alex.down()
    spiral(alex, 200, 0, -5)

    turtle.exitonclick()        # wait for a button click, then close window
    print("The window was closed. Bye!")


main()