from turtle import Turtle, Screen
import random

colors = ["red", "yellow", "orange", "green", "blue", "purple"]
turtles = []


def create_user_turtle(user_bet):
    user_turtle = Turtle(shape="turtle")
    user_turtle.color(user_bet)
    colors.remove(user_bet)
    turtles.append(user_turtle)


def create_turtles():
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtles.append(turtle)


def turtles_go_to_start():
    i = 0
    for turtle in turtles:
        turtle.up()
        turtle.goto(-200, -100 + 40*i)
        i += 1


def turtles_start_race():
    while True:
        for turtle in turtles:
            if turtle.xcor() < 230:
                turtle.forward(random.randint(0, 10))
            else:
                return turtle.pencolor()


def game():
    s = Screen()
    s.title("TURTLE RACE!!!")
    s.setup(width=500, height=400)
    user_bet = s.textinput(
        title="Make your bet.",
        prompt="Pick the color of your turtle (red/yellow/orange/green/blue/purple)")

    if user_bet in colors:
        create_user_turtle(user_bet)
        create_turtles()
        turtles_go_to_start()
        winner = turtles_start_race()
        if winner == user_bet:
            print(f"You've won! The {winner} turtle is the winner")
        else:
            print(f"You've lost. The {winner} turtle is the winner")
        s.exitonclick()
    else:
        s.bye()
        print("Invalid color.")


game()
