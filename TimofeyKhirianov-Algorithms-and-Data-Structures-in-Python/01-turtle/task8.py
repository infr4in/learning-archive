import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    x = 1
    while x < 30:
        t.forward(10*x)
        t.left(90)
        x += 1
    t.reset()
