import turtle as t

t.shape('turtle')


def flower(R, n):
    n_ang = 360 / n
    for i in range(round(n / 2)):
        t.circle(R)
        t.circle(-R)
        t.left(n_ang)


flower(60, 6)
