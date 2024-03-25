import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    x = 1
    while x < 11:
        for i in range(4):
            t.forward(10*x*2)
            t.left(90)
        t.penup()
        t.goto(-x*10, -x*10)
        t.pendown()
        x = x+1
    t.reset()
