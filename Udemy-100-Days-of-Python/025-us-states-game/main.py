import turtle as t
import pandas as pd


def draw_state(x, y, name):
    turtle.goto(x, y)
    turtle.write(name)


screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()


data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another stat?").title()
    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        x_cor = int(data[data["state"] == answer]["x"])
        y_cor = int(data[data["state"] == answer]["y"])
        draw_state(x_cor, y_cor, answer)





