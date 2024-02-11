from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(10)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, -295)
        for _ in range(15):
            self.goto(0, self.ycor() + 20)
            self.stamp()
            self.goto(0, self.ycor() + 20)

        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 72, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 72, "normal"))