import turtle as t

t.shape('turtle')


# R - радиус окружностей
# rx - шаг увеличения радиуса окружностей
# n - кол-во лепестков (четное)


def fly(R, rx, n):
    t.left(90)
    for i in range(round(n / 2)):
        t.circle(R)
        t.circle(-R)
        R += rx


fly(60, 10, 20)
