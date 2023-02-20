<h1 align="center">Space Invaders</h1>

<p align="center">
This is a copy-cat 'Space Invaders' game built with the Turtle library.</p>



## Links

- [Repo](https://github.com/kelseychristensen/Day-94-Space-Invaders "space-invaders")

## Screenshots

#### Invaders Moving
![Invaders Moving](/readme_gifs/invaders_move.gif "Invaders Moving")

#### Player Loses Life
![Player Loses Life](/readme_gifs/player_loses_life.gif "Player Loses Life")

#### Player Hits Invader
![Player Hits Invader](/readme_gifs/player_shoots.gif "Player Hits Invader")




### Built with

- Python
- Turtle Library

### What went into this project

This is a copy-cat space invaders game made with the Turtle library. I tried to use OOP as much as possible, with 7 classes included in the making of this game.

It includes three different styles of invader. It will record your high score. If you clear every invader, the game 'resets', but this time the invaders spawn closer to you. 

This project took several days and lots of troubleshooting -- trial and error, testing every possible variable. 

This was the type of project where I had to have print statements printing to the console after every time a loop would run telling me different statuses, variable values, list lengths etc. At one point, the solution to a problem I had been banging my head against for days was simply changing the text from "for item in invaders" to "for invader in invaders" and I'm not sure why. 

I particularly struggled with detecting a collision between the player's shots and an invader: for a long time, I could only get the shot to remove invaders from whatever was the top row at a time, I think because of when in the loop the collision detection occurred. Ultimately, I put this detection inside the Player class and that seemed to solve everything.

At the end of the day, this project took a lot of thinking both while coding it and in my days in between coding it, a lot of stepping away and coming back, and a lot of trial-and-error. 

### What I learned

For one thing, I learned how to add custom shapes to a Turtle app which was new for me and really allowed me to achieve the look I wanted this to have. 

### Continued development

There are two glitches that I would ideally prefer to be solved: 

1) Shooting a shot as the player interrupts the loop of an invader shooting and all the invaders scrolling to the left or right. 
2) Shooting a shot before a previous shot has hit an invader or made it off-screen makes the shot suspend on screen wherever it was when the additional shot was fired. 

I think both of these could probably be solved by playing with the orders of different loops, but I would love to know if it's possible to have multiple loops running independently of one another.

```python
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
```

## Author

Kelsey Christensen

- [Profile](https://github.com/kelseychristensen "Kelsey Christensen")
- [Email](mailto:kelsey.c.christensen@gmail.com?subject=Hi "Hi!")
- [Dribble](https://dribbble.com/kelseychristensen "Hi!")
- [Website](http://kelseychristensen.com/ "Welcome")
