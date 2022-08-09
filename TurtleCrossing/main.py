import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

SPEED = 0.1

game_on = True
while game_on:

    time.sleep(SPEED)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # check collision
    for i in cars.cars:
        if i.distance(player) < 20:
            print("collision")
            game_on = False

    if player.check_finish():
        score.update_score()
        SPEED /= 1.5

    score.get_score()

screen.exitonclick()