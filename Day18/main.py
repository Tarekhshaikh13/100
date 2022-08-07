
from turtle import Turtle, Screen

tim = Turtle()


def draw_shape(sides):
    angle = 360 / sides
    for side in range(sides):
        tim.forward(100)
        tim.right(angle)

 n
for i in range(3,11):
    draw_shape(i)







screen = Screen()
screen.exitonclick()