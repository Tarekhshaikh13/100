from turtle import *
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which Turtle will Win?")
is_race_on = False
colors = ["red", "yellow", "green", "orange", "blue", "purple"]

turtles = []
for i  in range(6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup(  )
    my_turtle.color(colors[i])
    turtles.append(my_turtle)

for i in range(6):
    my_turtle = turtles[i]
    my_turtle.goto(x= -230, y=150-i*50)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} is the Winner.")

            else:
                print(f"You've Lost.. The {turtle.pencolor()} is the Winner.")

        turtle.forward(random.randint(0,10))


screen.exitonclick()
