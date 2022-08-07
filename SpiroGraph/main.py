import turtle as t
import random
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def circles(my_turtle,size_of_gap):
    my_turtle.speed("fastest")

    for i in range(int(360/size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)

        my_turtle.setheading(my_turtle.heading()+ size_of_gap)


tim = t.Turtle()
circles(t, 10)

screen = t.Screen()
screen.exitonclick()
