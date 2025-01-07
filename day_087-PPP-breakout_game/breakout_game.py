from turtle import *

game = Turtle()

def right_key():
    forward(20)

def left_key():
    backward(20)

game.screen.onkeypress(right_key,"Right")
game.screen.onkeypress(left_key,"Left")

game.screen.listen()

game.screen.mainloop()