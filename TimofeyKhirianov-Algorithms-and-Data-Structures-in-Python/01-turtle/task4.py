import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)

while True:
    for i in range(360):
        t.forward(1)
        t.left(1)
    t.clear()
