from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):

    def __init__(self,k):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.shapesize(4, 1)
        self.setpos(k)

    def Up(self):
        self.speed('fastest')
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)


    def Down(self):
        self.speed('fastest')
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)

