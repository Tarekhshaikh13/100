from turtle import *

pace = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        for i in range(3):
            segment = Turtle(shape="circle")
            segment.penup()
            segment.color("white")
            segment.goto(x=-i*20, y=0)
            self.snake_body.append(segment)
        self.head = self.snake_body[0]

    def extend(self):
        segment = Turtle(shape="circle")
        segment.penup()
        segment.color("white")
        segment.goto(self.snake_body[-1].position())
        self.snake_body.append(segment)
        print("extended")

    def collision(self):
        for i in range(4, len(self.snake_body)):
            if self.head.distance(self.snake_body[i]) < 15:
                return True
        return False

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[seg - 1].xcor()
            y_cor = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x_cor, y_cor)
        x_head = self.head.xcor()
        y_head = self.head.ycor()

        if x_head < -280:
            self.head.goto(280,y_cor)
        elif x_head > 280:
            self.head.goto(-280,y_cor)
        elif y_head < -280:
            self.head.goto(x_cor,280)
        elif y_head > 280:
            self.head.goto(x_cor,-280)

        self.snake_body[0].forward(pace)

    def move_forward(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        #

    def move_backward(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def move_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def move_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)


