import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)

POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.score = 0

    def create_snake(self):
        for pos in POSITION:
            self.create_segment(pos)

    def create_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.speed(10)
        new_segment.penup()
        new_segment.color(change_color())
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def increase_length(self):
        new_segment = Turtle("square")
        new_segment.speed(10)
        new_segment.penup()
        new_segment.color(change_color())
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        self.border_check()

    def border_check(self):
        if (self.head.xcor()) > 300:
            self.head.goto(-300, 0)
        elif (self.head.ycor()) > 300:
            self.head.goto(0, -300)
        elif (self.head.xcor()) < -300:
            self.head.goto(300, 0)
        elif (self.head.ycor()) < -300:
            self.head.goto(0, 300)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
