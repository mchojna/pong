import turtle


class Screen:

    def __init__(self):
        self.screen = turtle.Screen()

    def create(self):
        self.screen.setup(width=1000, height=750)
        self.screen.bgcolor("black")
        self.screen.title("Pong")

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()

    def move(self, key, fun):
        self.screen.onkeyrelease(key=key, fun=fun)

    def exit(self):
        self.screen.exitonclick()


class Line:

    def __init__(self):
        self.line = None

    def create(self):
        y_cor = 335
        for _ in range(23):
            self.line = turtle.Turtle()
            self.line.hideturtle()
            self.line.penup()
            self.line.speed(0)
            self.line.color("white")
            self.line.shape("square")
            self.line.turtlesize(0.8, 0.2, 0)
            self.line.goto(x=0, y=y_cor)
            self.line.showturtle()

            y_cor -= 30
