
import turtle
from random import randint

turtle.width(5)
blue = True
state = 30

for i in range(2000):
    #turtle.left(randint(1,25))
    if state < 10:
        turtle.left(15)
    turtle.left(5)
    state -= 1
    if state <= 0:
        state = 30
    if blue:
        turtle.color('blue')
        turtle.forward(10)
        blue = False
        turtle.color('orange')
    else:
        turtle.forward(10)
        blue = True
