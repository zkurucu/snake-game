from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    
    


