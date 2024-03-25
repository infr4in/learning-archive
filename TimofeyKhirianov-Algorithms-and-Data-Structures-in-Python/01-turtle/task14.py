import turtle as t

t.shape('turtle')


def star(a, n):
    if (n % 2) == 0:
        print("Звезда должна иметь нечетное кол-во вершин")
    else:
        for i in range(n):
            t.forward(100)
            t.left(180 - 180 / n)


star(100, 11)
