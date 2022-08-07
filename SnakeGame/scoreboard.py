import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.setposition(0, 270)
        self.score = 0

    def get_score(self):
        self.write(f"Score:  {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.home()
        self.pencolor("blue")
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1