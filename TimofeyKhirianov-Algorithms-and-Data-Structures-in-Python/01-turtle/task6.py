import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    for i in range(12):
        t.right(360/12)
        t.forward(100)
        t.stamp()
        t.backward(100)
    t.clear()
