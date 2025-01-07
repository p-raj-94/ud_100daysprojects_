from turtle import Turtle

WINDOWS_HEIGHT = 600
MOVE_DISTANCE = 55

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.color("black")
        self.speed("fastest")
        self.on_start()

    def on_start(self):
        self.goto(0, -240)

    def right_key(self):
        if self.pos()[0] < int(WINDOWS_HEIGHT / 2) - 40:
            self.forward(MOVE_DISTANCE)

    def left_key(self):
        if self.pos()[0] > - int(WINDOWS_HEIGHT / 2) + 40 :
            self.backward(MOVE_DISTANCE)