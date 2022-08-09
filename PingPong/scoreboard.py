
from turtle import Turtle
import paddle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(270)
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.player1 = 0
        self.player2 = 0
        self.goto(0, 280)

    def get_score(self):
        self.write(f"{self.player1} :: {self.player2}", align="center", font=("Arial", 12, "normal"))

    def check_game_over(self):
        if self.player1 == 10:
            self.home()
            self.write(f"Player 1 Wins!", align="center", font=("Arial", 12, "normal"))
            return True
        elif self.player2 == 10:
            self.home()
            self.write(f"Player 2 Wins!", align="center", font=("Arial", 12, "normal"))
            return True
        return False

    def update_score(self):
        self.clear()
