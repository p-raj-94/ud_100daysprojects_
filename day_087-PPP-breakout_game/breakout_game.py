import turtle
import time
from brick import Brick
from ball import Ball
from player import Player

game = turtle.Screen()
game.setup(600, 600)
game.title('Turtle Breakout')
game.tracer(0)
screenx, screeny = game.window_width(), game.window_height()
player = Player()
ball = Ball()
""" bricks = Brick() """

game.listen()

game.onkeypress(player.right_key,"Right")
game.onkeypress(player.left_key,"Left")

playing_game = True
game_over = False

def check_collision_with_walls():
    global ball, game_over

    # detect collision with left and right walls:
    if ball.xcor() < -screenx/2 + 15 or ball.xcor() > screenx/2 - 15:
        ball.bounce(True, False)
        return

    if ball.ycor() > screeny/2 - 15:
        ball.bounce(False,True)
        return
    
    if ball.ycor() < -screeny/2 + 15:
        ball.init_ball()
        return
    

def check_collision_with_player():
    global ball, player

    playerx = player.xcor()
    ball_x = ball.xcor()

    if ball.distance(player) < 55 and ball.ycor() < -230:
        if ball_x > playerx:
            if ball.x_move_dist > 0: 
                ball.bounce(False, True)
                return
            else:
                ball.bounce(True, True)
                return
        elif ball_x < playerx:
            if ball.x_move_dist > 0: 
                ball.bounce(True, True)
                return
            else:
                ball.bounce(False, True)
                return
        else:
            ball.bounce(False, True)
            return
        

while playing_game:
    game.update()
    time.sleep(0.04)

    ball.move()

    check_collision_with_walls()
    check_collision_with_player()

game.mainloop()
