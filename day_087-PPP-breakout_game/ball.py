from turtle import Turtle
import random


WINDOWS_HEIGHT = 600
X_SPEED = 9
class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move_dist = 10
        self.y_move_dist = 6
        self.init_ball()
        
    def move(self):
        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(new_x, new_y)

    def bounce(self, xbounce, ybounce, ballplayer_x):
        if ballplayer_x == self.x_move_dist:
            if  ballplayer_x < 17:
                self.x_move_dist = 6 if self.x_move_dist > 0 else -6
            elif ballplayer_x < 35:
                self.x_move_dist = 10 if self.x_move_dist > 0 else -10
            else:
                self.x_move_dist = 15 if self.x_move_dist > 0 else -15

        if xbounce:
            self.x_move_dist *= -1

        if ybounce:
            self.y_move_dist *= -1


    def init_ball(self):
        self.goto(0, -int(WINDOWS_HEIGHT / 2) + 90)
        self.y_move_dist = 10