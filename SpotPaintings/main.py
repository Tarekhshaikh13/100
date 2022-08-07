
import turtle as t
import random


color_list = [(47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29),
              (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96),
              (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
              (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
t.hideturtle()
t.colormode(255)


def spot_painting(my_turtle, dotsize, blocksize):
    my_turtle.speed("fastest")

    for columns in range(blocksize):
        current_position = my_turtle.position()
        for rows in range(blocksize):
            my_turtle.dot(dotsize, random.choice(color_list))

            my_turtle.penup()
            my_turtle.forward(dotsize*2)

        my_turtle.setposition(current_position)

        my_turtle.left(90)
        my_turtle.forward(dotsize*2)
        my_turtle.right(90)


tim = t.Turtle()

tim.hideturtle()
tim.penup()
tim.goto(-650, -350)
tim.pendown()

spot_painting(tim, 10, 25)

screen = t.Screen()
screen.exitonclick()
