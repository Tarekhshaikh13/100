from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import time
import scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Arcade")
screen.tracer(0)




player1 = Paddle()
player1.goto(350, 0)

player2 = Paddle()
player2.goto(-350, 0)

pong = Pong()

score = scoreboard.ScoreBoard()


screen.listen()
screen.onkey(player1.move_up,  "Up")
screen.onkey(player1.move_down, "Down")


screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")


while True:
    screen.update()
    time.sleep(0.1)
    pong.move()
    score.get_score()

    if pong.ycor() > 275 or pong.ycor() < -275:
        pong.bounce()

    if pong.distance(player1) < 50 and pong.xcor() > 320 or pong.distance(player2) < 50 and pong.xcor() < -320:
        print("made contact")
        pong.turn_direction()

    if pong.xcor() > 380:
        print("player 1 miss")
        score.player1 += 1
        score.update_score()
        pong.reset_pong()

    if pong.xcor() < -380:
        print("player 2 miss")
        score.player2 += 1
        score.update_score()
        pong.reset_pong()

    if score.check_game_over():
        break















screen.exitonclick()