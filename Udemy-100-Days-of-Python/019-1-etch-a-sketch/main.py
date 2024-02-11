from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def clear_all():
    t.clear()
    t.up()
    t.home()
    t.down()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


s.listen()
s.onkeypress(key="w", fun=move_forward)
s.onkeypress(key="s", fun=move_backward)
s.onkeypress(key="a", fun=turn_left)
s.onkeypress(key="d", fun=turn_right)
s.onkeypress(key="c", fun=clear_all)

s.exitonclick()
