from screen import Screen, Line
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.listen()

line = Line()

scoreboard = ScoreBoard()

player_1 = Paddle(x_cor=440, y_cor=0)
player_2 = Paddle(x_cor=-450, y_cor=0)

ball = Ball()

screen.move(key="Up", fun=player_1.move_up)
screen.move(key="Down", fun=player_1.move_down)

screen.move(key="w", fun=player_2.move_up)
screen.move(key="s", fun=player_2.move_down)

screen.create()

line.create()

player_1.create()
player_2.create()

pong = True

while pong:

    scoreboard.create()

    ball.create()
    ball.random()

    game = True

    while game:

        ball.move()

        if ball.ycor() > 355 or ball.ycor() < -345:
            ball.bounce_y()

        if ball.xcor() <= -495:
            scoreboard.player_1_score += 1
            game = False
            break

        if ball.xcor() >= 495:
            scoreboard.player_2_score += 1
            game = False
            break

        if ball.distance(player_1) <= 50 and ball.xcor() >= 420:

            ball.bounce_x()

        if ball.distance(player_2) <= 50 and ball.xcor() >= -490:
            ball.bounce_x()

        screen.update()

    if scoreboard.player_1_score == 2 or scoreboard.player_2_score == 2 or (scoreboard.player_1_score == 2 and scoreboard.player_2_score == 2):
        scoreboard.end(scoreboard.player_1_score, scoreboard.player_2_score)
        pong = False
        break

screen.exit()
