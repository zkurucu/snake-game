from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}   Highest Score:{self.highest_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    
    


