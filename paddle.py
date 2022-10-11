from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.hideturtle()
        self.penup()

    def create(self):
        self.setpos(self.x_cor, self.y_cor)
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1, 0)
        self.showturtle()
        self.speed(1.25)

    # def move(self):
    #     self.setpos(self.x_cor, 300)
    #     self.setpos(self.x_cor, -290)

    def move_up(self):
        if not self.ycor() >= 300:
            self.goto(self.x_cor, (self.ycor() + 20))

    def move_down(self):
        if not self.ycor() <= -290:
            self.goto(self.x_cor, (self.ycor() - 20))



