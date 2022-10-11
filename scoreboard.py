from turtle import Turtle
import time


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0

    def create(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(-75, 270)
        self.clear()
        self.write(arg=f"{self.player_1_score}", align="center", font=("Super Effective", 110, "normal"))
        self.setpos(90, 270)
        self.write(arg=f"{self.player_2_score}", align="center", font=("Super Effective", 110, "normal"))


    def end(self, player_1_score, player_2_score):
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(0, 20)
        self.color("white")
        self.write(arg="Game Over!", align="center", font=("Super Effective", 100, "normal"))
        self.goto(0, -60)
        if player_1_score > player_2_score:
            winner = "Player 1 wins!"
        elif player_2_score > player_1_score:
            winner = "Player 2 wins!"
        else:
            winner = "Draw!"
        time.sleep(0.5)
        self.write(arg=f"{winner}", align="center", font=("Super Effective", 80, "normal"))
