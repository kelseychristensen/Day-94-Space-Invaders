from turtle import Turtle
from shot import EnemyShot

class Invader(Turtle):

    def __init__(self, cor, shape, screen):
        super().__init__()
        self.screen = screen
        self.shape(shape)
        self.penup()
        self.goto(cor)
        self.x_move = 20
        self.y_move = 20

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor()-self.x_move, new_y)
        self.reverse()

    def reverse(self):
        self.x_move *= -1

    def shoot(self):
        self.new_shot = EnemyShot(self)
        while self.new_shot.ycor() > -410:
            self.screen.update()
            self.new_shot.enemy_shot_move()
