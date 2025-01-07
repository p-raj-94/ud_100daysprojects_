from turtle import Turtle
import random

class Brick:
    
    def __init__(self):
        self.segments = []
        while len(self.segments) < 20:
            self.create_bricks()
        

    def create_bricks(self):
        brick = Turtle()
        brick.shape("square")
        brick.penup()
        brick.shapesize(stretch_len=2, stretch_wid=0.5)
        brick.color("blue")
        brick.speed("fastest")
        random_x = random.randint(-240, 240)
        random_y = random.randint(100, 240)
        brick.goto(random_x, random_y)
        self.segments.append(brick)
