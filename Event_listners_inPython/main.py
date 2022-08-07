from turtle import *

tim = Turtle()

tim.speed("fastest")
screen = Screen()


def move_forward():
    tim.setheading(90)
    tim.forward(25)


def move_backward():
    tim.setheading(90)
    tim.backward(25)
    tim.setheading(270)


def move_right():
    tim.setheading(90)
    tim.right(90)
    tim.forward(25)


def move_left():
    tim.setheading(90)
    tim.left(90)
    tim.forward(25)


def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "c")

screen.exitonclick()