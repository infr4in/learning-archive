import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.creating_cars()
    car_manager.move_cars()

    # Detect collision with the finish line
    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.increase_lvl()
        car_manager.lvl_up()

    # Detect collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
