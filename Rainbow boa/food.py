import random
from turtle import Turtle
from snake import change_color


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(change_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(change_color())
        self.goto(random_x, random_y)
