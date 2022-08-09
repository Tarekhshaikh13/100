from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-295, 250)
        self.hideturtle()
        self.score = 1


    def get_score(self):
        self.write(f"level : {self.score}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.score +=1

