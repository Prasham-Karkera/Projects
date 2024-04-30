from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self,k):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(k)
        self.write("Score = 0", False, align=ALIGNMENT, font=FONT)

    def add(self,i):
        self.clear()
        self.write(f"Score = {i}", False, align=ALIGNMENT, font=FONT)

    def gameover(self,s):
        self.goto(0,0)
        self.write(f"GAME OVER, {s} wins !!!", False, align=ALIGNMENT, font=FONT)
