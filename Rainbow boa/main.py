import time
from food import Food
from snake import Snake
from turtle import Screen, Turtle
from snake import change_color
from scoreBoard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Rainbow Boa")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.score += 1
        score.show_score()
        snake.create_segment(snake.segments[-1].position())
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False
        screen.exitonclick()

    for seg in snake.segments[1:-1]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_is_on = False
            screen.exitonclick()