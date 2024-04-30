from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)


s = Snake()
f = Food()
score = Scoreboard()
scr.listen()
scr.onkey(s.up, "Up")
scr.onkey(s.down, "Down")
scr.onkey(s.left, "Left")
scr.onkey(s.right, "Right")

game_is_on = True
c = 0
while game_is_on:
    s.move()
    scr.update()
    time.sleep(0.1)

    #Detect collision with food
    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        c += 1
        score.add(c)

    #Detect collision with the wall
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detect collision with tail
    for i in s.segments[1:]:
        if s.head.distance(i) < 10:
            score.game_over()
            game_is_on = False


scr.exitonclick()
