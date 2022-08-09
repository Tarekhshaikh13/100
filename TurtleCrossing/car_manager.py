from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_cars(self):
        if random.randint(1, 6) == 6:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor )

            self.cars.append(car)

    def move_cars(self):
        for i in self.cars:
            i.backward(MOVE_INCREMENT)

        # remove cars once it crosses screen
        for i in self.cars:
            if i.xcor() < -300:
                i.hideturtle()
                self.cars.remove(i)



