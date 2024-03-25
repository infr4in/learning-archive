import turtle as t

t.shape('turtle')


def spring(R, n):
    t.left(90)
    for i in range(n):
        t.circle(-R, 180)
        t.circle(-R / 5, 180)


spring(30, 6)
