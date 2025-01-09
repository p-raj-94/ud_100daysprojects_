import turtle
import time
from brick import Bricks
from ball import Ball
from player import Player

game = turtle.Screen()
game.setup(600, 600)
game.title('Turtle Breakout')
game.tracer(0)
screenx, screeny = int(game.window_width() / 2,), int(game.window_height() / 2)
player = Player()
ball = Ball()
bricks = Bricks()
game.listen()

def start_game():
    global game_over
    game_over = False
    

game.onkeypress(player.right_key,"Right")
game.onkeypress(player.left_key,"Left")
game.onkeypress(start_game, "space" )

playing_game = True
game_over = True

game_ui = turtle.Turtle()
game_ui.hideturtle()
game_ui.penup()
game_ui.goto(0, -100)


def check_collision_with_walls():
    global ball, game_over

    # detect collision with left and right walls:
    if ball.xcor() < -screenx + 10 or ball.xcor() > screenx - 25:
        ball.bounce(True, False, ball.x_move_dist)
        return

    if ball.ycor() > screeny - 15:
        ball.bounce(False,True, ball.x_move_dist)
        return
    
    # collision with bottom wall
    if ball.ycor() < -screeny+25 :
        game_over = True
        ball.init_ball()
        return
    

def check_collision_with_player():
    global ball, player

    playerx = player.xcor()
    ball_x = ball.xcor()

    if abs(abs(ball.xcor() - player.xcor())) < 60 and ball.ycor() < player.ycor() + 35:
        ballplayer_x = abs(ball.xcor() - player.xcor())
        if ball_x > playerx:
            if ball.x_move_dist > 0: 
                ball.bounce(False, True,ballplayer_x)
                return
            else:
                ball.bounce(True, True,ballplayer_x)
                return
        elif ball_x < playerx:
            if ball.x_move_dist > 0: 
                ball.bounce(True, True,ballplayer_x)
                return
            else:
                ball.bounce(False, True,ballplayer_x)
                return
        else:
            ball.bounce(False, True,ballplayer_x)
            return
    

def check_collision_with_bricks():
    global ball, bricks

    ball_x = ball.xcor()

    for brick in bricks.bricks:
        brick_x = brick.xcor()
        if abs(brick_x - ball_x) < 60 and abs(brick.ycor() - ball.ycor()) < 30:
            if ball_x > brick_x:
                if ball.x_move_dist > 0: 
                    ball.bounce(False, True, ball.x_move_dist)
                else:
                    ball.bounce(True, True, ball.x_move_dist)         
            elif ball_x < brick_x:
                if ball.x_move_dist > 0: 
                    ball.bounce(True, True, ball.x_move_dist)
                else:
                    ball.bounce(False, True, ball.x_move_dist)
                    
            else:
                ball.bounce(False, True, ball.x_move_dist)
                

            brick.hideturtle()
            brick.goto(0,1000)
            return
            


while playing_game:
    game.update()
    time.sleep(0.04)

    

    check_collision_with_walls()
    check_collision_with_bricks()
    if not game_over:
        ball.move()
        check_collision_with_player()
        game_ui.clear()
    else:
        ball.goto(player.xcor(), -screeny + 90)
        game_ui.write('Press Space to throw ball',align='center', font=('Calibri', 20, 'bold'))

game.mainloop()
