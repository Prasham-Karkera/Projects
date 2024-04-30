from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
scr = Screen()

scr.title('Pong')
scr.setup(800, 600)
scr.bgcolor('black')
scr.tracer(0)

score_a = Scoreboard((-200,270))
score_b = Scoreboard((200,270))
r_p = Paddle((350, 0))
l_p = Paddle((-350, 0))
ball = Ball()
game_is_on = True

scr.listen()
scr.onkey(r_p.Up, "Up")
scr.onkey(r_p.Down, "Down")
scr.onkey(l_p.Up, "w")
scr.onkey(l_p.Down, "s")

a = 0
b = 0
i = 0
while game_is_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()


    #Detect collision with right paddle
    if ball.distance(r_p) < 40 and ball.xcor() > 310 or ball.distance(l_p) < 40 and ball.xcor() < -310:
        ball.paddle_bounce()


    #Detect collision with wall
    if ball.xcor() > 400:
        ball.reset_position()
        a += 1
        score_a.add(a)
    elif ball.xcor() < -400:
        ball.reset_position()
        b += 1
        score_b.add(b)

    #GameOver
    if a == 10:
        score_a.gameover("A")
        game_is_on = False
    elif b == 10:
        score_b.gameover("B")
        game_is_on = False



scr.exitonclick()
