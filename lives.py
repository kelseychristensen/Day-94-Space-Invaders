from turtle import Turtle
ALIGNMENT = "left"
FONT = ('Courier', 14, 'normal')

class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(80, 350)
        self.update()

    def update(self):
        self.clear()
        lives_emoji = "🕹️"
        to_write = lives_emoji * self.lives
        self.write(f"Lives: {to_write}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.lives = 3
        self.update()

    def lose_life(self):
        self.clear()
        self.lives -= 1
        self.update()