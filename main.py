from turtle import Screen
from invaders import Invader
from scoreboard import Scoreboard
from lives import Lives
from player import Player
import random
import time

invaders = []
start_y = 300

def create_invaders():
    invader_1_y_cors = [start_y, start_y - 50]
    invader_2_y_cors = [start_y - 100, start_y - 150]
    invader_3_y_cors = [start_y - 200, start_y - 250]
    x_cors = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

    for y_cor in invader_1_y_cors:
        for x_cor in x_cors:
            new_invader = Invader((x_cor, y_cor), invader_1, screen)
            invaders.append(new_invader)

    for y_cor in invader_2_y_cors:
        for x_cor in x_cors:
            new_invader = Invader((x_cor, y_cor), invader_2, screen)
            invaders.append(new_invader)

    for y_cor in invader_3_y_cors:
        for x_cor in x_cors:
            new_invader = Invader((x_cor, y_cor), invader_3, screen)
            invaders.append(new_invader)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Space Invaders")
screen.tracer(0)
time.sleep(1)

invader_1 = "invader1.gif"
invader_2 = "invader2.gif"
invader_3 = "invader3.gif"
player_shape = "player.gif"

screen.addshape(invader_1)
screen.addshape(invader_2)
screen.addshape(invader_3)
screen.addshape(player_shape)

create_invaders()
scoreboard = Scoreboard()
player = Player(player_shape, screen, invaders, scoreboard)
lives = Lives()

screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkey(player.shoot, "space")

game_is_on = True
invaders_should_move = True

while game_is_on:

    screen.update()

    # MOVE INVADERS TO THE LEFT/RIGHT
    # DETECT IF INVADERS HAVE REACHED PLAYER

    for invader in invaders:
        invader.move()
        if invader.ycor() <= -300:
            lives.lose_life()

    # MOVE INVADERS DOWN AND REVERSE DIRECTION
    for invader in invaders:
        if invader.xcor() > 350 or invader.xcor() < -350:
            for invader in invaders:
                invader.move_down()

    time.sleep(1)

    # DETERMINE WHICH INVADER SHOULD SHOOT

    shooting_invader = random.choice(invaders)
    shooting_invader.shoot()

    # DETECT COLLISION OF ENEMY SHOT WITH PLAYER
    # REMOVE LIFE UPON COLLISION

    if player.distance(shooting_invader.new_shot) < 115:
        reset_y = player.ycor()
        reset_x = player.xcor()
        lives.lose_life()
        for number in range(3):
            screen.update()
            time.sleep(.1)
            player.goto(500, 500)
            screen.update()
            time.sleep(.1)
            player.goto(reset_x, reset_y)


    # DETECT IF NEXT LEVEL SHOULD BEGIN

    if len(invaders) == 0:
        player.reset()
        scoreboard.reset()
        start_y -= 50
        create_invaders()
        screen.update()

    # DETECT GAME OVER AND RESET

    if lives.lives == 0:
        player.reset()
        scoreboard.reset()
        lives.reset()
        for invader in invaders:
            invader.goto(500, 500)
        invaders = []
        create_invaders()
        screen.update()

screen.exitonclick()
