from turtle import Turtle

class EnemyShot(Turtle):

    def __init__(self, invader):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.2, stretch_len=.2)
        self.color("lime")
        self.goto(invader.xcor(), invader.ycor())
        self.y_move = 5

    def enemy_shot_move(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)

