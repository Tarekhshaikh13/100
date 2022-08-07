from turtle import Screen
import time
import snake as s
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("The Snake Arcade")

snake = s.Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.move_forward, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_backward, "Down")

while True:
    screen.update()
    time.sleep(0.15)

    if snake.head.distance(food) < 20:
        scoreboard.update_score()
        snake.extend()
        food.refresh()
    scoreboard.get_score()
    if snake.collision():
        scoreboard.game_over()
        break
    snake.move()








screen.exitonclick()