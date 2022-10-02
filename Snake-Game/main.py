from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key="Down")
screen.onkey(fun = snake.left, key="Left")
screen.onkey(fun = snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    
    ###Detecting  collision between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    ###Detecting snake collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
        
    ###Detecting snake collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()