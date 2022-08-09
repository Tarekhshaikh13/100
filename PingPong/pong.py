from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(1, 1)
        self.penup()
        self.speed("normal")
        self.x_move = 10
        self.y_move = 10

    def turn_direction(self):
        self.x_move = - self.x_move

    def bounce(self):
        self.y_move = - self.y_move

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def reset_pong(self):
        self.home()
        self.x_move = - self.x_move
