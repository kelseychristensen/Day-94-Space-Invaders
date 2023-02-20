from turtle import Turtle
from player_shot import PlayerShot

class Player(Turtle):

    def __init__(self, shape, screen, invaders, scoreboard):
        super().__init__()
        self.invaders = invaders
        self.scoreboard = scoreboard
        self.screen = screen
        self.shape(shape)
        self.penup()
        self.goto(0, -300)
        self.y_move = 50

    def left(self):
        y_cor = self.ycor()
        x_cor = self.xcor() - 5
        self.goto(x_cor, y_cor)

    def right(self):
        y_cor = self.ycor()
        x_cor = self.xcor() + 5
        self.goto(x_cor, y_cor)

    def reset(self):
        self.goto((0, -300))

    def shoot(self):
        self.new_shot = PlayerShot(self, self.invaders, self.scoreboard)
        while self.new_shot.ycor() < 410:
            # DETECT COLLISION OF PLAYER SHOT WITH INVADER
            # AWARD POINTS UPON COLLISION
            for invader in self.invaders:
                if invader.distance(self.new_shot) < 40:
                    self.scoreboard.add_point()
                    invader.goto(500, 500)
                    self.invaders.remove(invader)
                    self.new_shot.goto(500, 500)
            # MOVE SHOT UPWARDS UNTIL IT'S OFFSCREEN
            self.screen.update()
            self.new_shot.move()


