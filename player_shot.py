from turtle import Turtle

class PlayerShot(Turtle):

    def __init__(self, player, invaders, scoreboard):
        super().__init__()
        self.invaders = invaders
        self.scoreboard = scoreboard
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.2, stretch_len=.2)
        self.color("yellow")
        self.goto(player.xcor(), player.ycor())
        self.y_move = 5

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)