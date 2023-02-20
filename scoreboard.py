from turtle import Turtle
ALIGNMENT = "left"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-260, 350)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as data:
                data.write(str(self.high_score))
            self.update()

    def add_point(self):
        self.clear()
        self.current_score += 1
        self.update()

