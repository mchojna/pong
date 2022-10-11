from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_add = 0
        self.y_add = 0

    def create(self):
        self.hideturtle()
        self.penup()
        self.setpos(0, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(2)
        self.speed("normal")
        self.showturtle()

    def random(self):
        self.x_add = random.randint(-10, 10)
        self.y_add = random.randint(-10, 10)

    def move(self):
        self.goto(self.xcor() + self.x_add, self.ycor() + self.y_add)

    def bounce_y(self):
        self.y_add *= -1

    def bounce_x(self):
        self.x_add *= -1


