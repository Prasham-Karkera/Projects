from turtle import Turtle

class Ball(Turtle):

    def  __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1,1)
        self.color('white')
        self.penup()
        self.move_speed = 0.05
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed -= 0.001

    def reset_position(self):
        self.setpos(0,0)
        self.x_move *= -1
        self.move_speed = 0.05

