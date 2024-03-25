import turtle
import math

t = turtle
t.shape('turtle')

# Нарисовать n вложенных правильных многоугольников
# R - радиус окружность / длина стороны фигуры
# rx - отступ между фигурами
# n - кол-во многоугольников


def mnogoug(R, rx, n):
    for i in range(3, n + 3):
        ang = 360 / i                      # угол между вершинами фигуры
        a = 2 * R * math.sin(math.pi / i)  # длина стороны фигуры
        obj_move_ang = (180 - ang) / 2     # угол поворота фигуры
        t.right(obj_move_ang)              # поворот фигуры
        for j in range(i):                 # цикл построения фигуры
            t.right(ang)
            t.forward(a)
        t.left(obj_move_ang)               # возврат черепахи в исходное состояние
        t.penup()
        t.forward(rx * (i - j))            # отступ между фигурами
        t.pendown()
        R += rx                            # увеличиваем радиус на отступ


mnogoug(10, 20, 100)
