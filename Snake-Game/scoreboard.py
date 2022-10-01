from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=275)
        self.cur_score = 0
        self.update_screen()
        
    def update_screen(self):
        self.write(f"Score: {self.cur_score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.home()
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.cur_score += 1
        self.update_screen()