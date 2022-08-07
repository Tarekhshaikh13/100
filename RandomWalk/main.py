import turtle
import random
from colors import colors


angles = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk(my_turtle):
    my_turtle.pensize(5)
    my_turtle.setheading(random.choice(angles))
    my_turtle.speed("fastest")
    my_turtle.hideturtle()
    for i in range(1000):
        random_color()
        my_turtle.right(random.choice(angles))
        my_turtle.color(random_color())
        my_turtle.forward(20)


tim = turtle.Turtle()
random_walk(tim)

screen = turtle.Screen()
screen.exitonclick()