import turtle
import sys

sam = turtle.Turtle()

def square(size,color):
    sam.fillcolor(color)
    sam.begin_fill()
    x=0
    while x < 4:
        sam.forward(size)
        sam.left(90)
        x+=1
    sam.end_fill()

# draw a circle
def circle(size,color):
    sam.fillcolor(color)
    sam.begin_fill()
    sam.circle(size)
    sam.end_fill()

# triangle
def triangle(size,color):
    sam.fillcolor(color)
    sam.begin_fill()
    x = 0
    while x < 3:
        sam.forward(size)
        sam.left(120)
        x += 1
    sam.end_fill

#  star
def star(size,color):
    sam.fillcolor(color)
    sam.begin_fill()
    x = 0
    while x < 5:
        sam.forward(size)
        sam.right(144)
        x += 1
    sam.end_fill()

# circle(100,"magenta")
# triangle(200,"black")
# star(300,"blue")

shape = raw_input("Would you like a circle, a square, a star, or a triangle? >>")
color = raw_input("What color would you like the shape to be? >>")
size = raw_input("How big do you want it to be? (1-500) >>")


if shape == "circle":
    circle(int(size),color)

if shape == "star":
    star(int(size),color)

if shape == "triangle":
    triangle(int(size),color)

if shape == "square":
    square(int(size),color)

# get the user's choice for shape, size and color

# call the appropiate function with the correct parameters


turtle.done()
