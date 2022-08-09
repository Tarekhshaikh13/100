from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(1, 5)


    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)

