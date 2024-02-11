from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.cars_move_speed = STARTING_MOVE_DISTANCE

    def creating_cars(self):
        if random.randint(1, 6) == 1:
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -320:
                car.car_move(self.cars_move_speed)
            else:
                car.clear()
                car.hideturtle()
                self.cars.pop(self.cars.index(car))

    def lvl_up(self):
        for car in self.cars:
            car.clear()
            car.hideturtle()
        self.cars = []
        self.cars_move_speed += MOVE_INCREMENT


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.setposition(320, random.randint(-250, 250))

    def car_move(self, move_speed):
        self.forward(move_speed)
