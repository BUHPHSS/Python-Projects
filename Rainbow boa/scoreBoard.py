from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: 0", align="center", font=("Verdana", 15, "bold"))

    def show_score(self):
        self.clear()
        self.penup()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align= "Center", font=("Verdana", 25, "bold"))
