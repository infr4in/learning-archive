import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    for i in range(2):
        t.forward(50)
        t.left(90)
    for i in range(2):
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(180)
        t.clear()
