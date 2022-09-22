# following tutorial from: https://medium.com/nerd-for-tech/programming-fractals-in-python-d42db4e2ed33

import turtle

def koch_fract(turtle, divis, size):
    if(divis == 0):
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)
            turtle.forward(2)
            turtle.left(angle)


# variables for koch_fract function
divis = 10
size = 1


# setting up turtle
wn = turtle.Screen()
wn.setup()
turtle.speed(500)
turtle.pendown()


for i in range(0, 3):
   koch_fract(turtle, divis, size)
