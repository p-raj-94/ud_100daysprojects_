from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move_dist = 10
        self.y_move_dist = 10
        self.init_ball()
        
    def move(self):
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(new_x, new_y)

    def bounce(self, xbounce, ybounce):
        if xbounce:
            self.x_move_dist *= -1

        if ybounce:
            self.y_move_dist *= -1


    def init_ball(self):
        self.goto(0, -210)
        self.y_move_dist = 10