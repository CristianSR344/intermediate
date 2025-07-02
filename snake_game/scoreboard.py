from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.score()

    
    def score(self):
        self.write(f"Score: {self.count}", align= ALIGNMENT, font=FONT)
        
    def score_up(self):
        self.count += 1
        self.clear()
        self.score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= ALIGNMENT, font=FONT)
        
    