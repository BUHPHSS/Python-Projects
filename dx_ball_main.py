import turtle

wn = turtle.Screen()
wn.title("Dx Ball")
wn.bgcolor("black")
wn.setup(width=400, height=400)
wn.tracer(0)

# Score and Lives
score = 0
lives = 3
bricks = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -150)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -130)
ball.dx = 0.3
ball.dy = 0.3

# Pen for score
pen_score = turtle.Turtle()
pen_score.speed(0)
pen_score.color("white")
pen_score.penup()
pen_score.hideturtle()
pen_score.setposition(130, 170)
pen_score.write("Score: 0", align="center", font=("Courier", 12, "normal"))

# Pen for lives
pen_lives = turtle.Turtle()
pen_lives.speed(0)
pen_lives.color("white")
pen_lives.penup()
pen_lives.hideturtle()
pen_lives.setposition(-140, 170)
pen_lives.write("Lives: 3", align="center", font=("Courier", 12, "normal"))

# Pen for other
pen_other = turtle.Turtle()
pen_other.speed(0)
pen_other.color("white")
pen_other.penup()
pen_other.hideturtle()

# Brick class
class Brick:

    def __init__(self, x_cor, y_cor, point, colour):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.point = point
        self.colour = colour
        self.turtle_object = turtle.Turtle()
        self.turtle_object.speed(0)
        self.turtle_object.shape("square")
        self.turtle_object.color("black", colour)
        self.turtle_object.shapesize(stretch_wid=1, stretch_len=3)
        self.turtle_object.penup()
        self.turtle_object.goto(x_cor, y_cor)

    def disappear(self):
        self.turtle_object.hideturtle()


# Bricks
brick_1 = Brick(-120, 150, 10, "white")
brick_2 = Brick(-60, 150, 10, "white")
brick_3 = Brick(0, 150, 10, "white")
brick_4 = Brick(60, 150, 10, "white")
brick_5 = Brick(120, 150, 10, "white")
brick_6 = Brick(-120, 130, 10, "white")
brick_7 = Brick(-60, 130, 10, "white")
brick_8 = Brick(0, 130, 10, "white")
brick_9 = Brick(60, 130, 20, "red")
brick_10 = Brick(120, 130, 10, "white")
brick_11 = Brick(-120, 110, 20, "red")
brick_12 = Brick(-60, 110, 10, "white")
brick_13 = Brick(0, 110, 10, "white")
brick_14 = Brick(60, 110, 10, "white")
brick_15 = Brick(120, 110, 10, "white")
brick_16 = Brick(-120, 90, 10, "white")
brick_17 = Brick(-60, 90, 10, "white")
brick_18 = Brick(0, 90, 20, "red")
brick_19 = Brick(60, 90, 10, "white")
brick_20 = Brick(120, 90, 10, "white")
brick_21 = Brick(-120, 70, 10, "white")
brick_22 = Brick(-60, 70, 10, "white")
brick_23 = Brick(0, 70, 10, "white")
brick_24 = Brick(60, 70, 10, "white")
brick_25 = Brick(120, 70, 10, "white")

brick_1_existence = True
brick_2_existence = True
brick_3_existence = True
brick_4_existence = True
brick_5_existence = True
brick_6_existence = True
brick_7_existence = True
brick_8_existence = True
brick_9_existence = True
brick_10_existence = True
brick_11_existence = True
brick_12_existence = True
brick_13_existence = True
brick_14_existence = True
brick_15_existence = True
brick_16_existence = True
brick_17_existence = True
brick_18_existence = True
brick_19_existence = True
brick_20_existence = True
brick_21_existence = True
brick_22_existence = True
brick_23_existence = True
brick_24_existence = True
brick_25_existence = True


# Function
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for ball
    if ball.xcor() > 175:
        ball.setx(175)
        ball.dx *= -1

    if ball.xcor() < -175:
        ball.setx(-175)
        ball.dx *= -1

    if ball.ycor() > 175:
        ball.sety(175)
        ball.dy *= -1

    if ball.ycor() < -175:
        ball.setposition(paddle.xcor(), paddle.ycor())
        ball.dy *= -1
        lives -= 1
        pen_lives.clear()
        pen_lives.write(f"Lives: {lives}", align="center", font=("Courier", 12, "normal"))

    # Border checking for paddle
    if paddle.xcor() > 140:
        paddle.setx(140)
        #ball.dx *= -1

    if paddle.xcor() < -140:
        paddle.setx(-140)
        #ball.dx *= -1

    # Paddle and ball collision
    if paddle.ycor() < ball.ycor() < paddle.ycor() + 20 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
        ball.sety(-130)
        ball.dy *= -1

    # Brick 1
    if brick_1_existence:
        if brick_1.y_cor - 20 < ball.ycor() < brick_1.y_cor + 20 and brick_1.x_cor - 30 < ball.xcor() < brick_1.x_cor + 30:
            brick_1.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_1_existence = False
            bricks += 1
            score += brick_1.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))


    # Brick 2
    if brick_2_existence:
        if brick_2.y_cor - 20 < ball.ycor() < brick_2.y_cor + 20 and brick_2.x_cor - 30 < ball.xcor() < brick_2.x_cor + 30:
            brick_2.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_2_existence = False
            bricks += 1
            score += brick_2.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 3
    if brick_3_existence:
        if brick_3.y_cor - 20 < ball.ycor() < brick_3.y_cor + 20 and brick_3.x_cor - 30 < ball.xcor() < brick_3.x_cor + 30:
            brick_3.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_3_existence = False
            bricks += 1
            score += brick_3.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 4
    if brick_4_existence:
        if brick_4.y_cor - 20 < ball.ycor() < brick_4.y_cor + 20 and brick_4.x_cor - 30 < ball.xcor() < brick_4.x_cor + 30:
            brick_4.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_4_existence = False
            bricks += 1
            score += brick_4.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 5
    if brick_5_existence:
        if brick_5.y_cor - 20 < ball.ycor() < brick_5.y_cor + 20 and brick_5.x_cor - 30 < ball.xcor() < brick_5.x_cor + 30:
            brick_5.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_5_existence = False
            bricks += 1
            score += brick_5.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 6
    if brick_6_existence:
        if brick_6.y_cor - 20 < ball.ycor() < brick_6.y_cor + 20 and brick_6.x_cor - 30 < ball.xcor() < brick_6.x_cor + 30:
            brick_6.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_6_existence = False
            bricks += 1
            score += brick_6.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 7
    if brick_7_existence:
        if brick_7.y_cor - 20 < ball.ycor() < brick_7.y_cor + 20 and brick_7.x_cor - 30 < ball.xcor() < brick_7.x_cor + 30:
            brick_7.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_7_existence = False
            bricks += 1
            score += brick_7.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 8
    if brick_8_existence:
        if brick_8.y_cor - 20 < ball.ycor() < brick_8.y_cor + 20 and brick_8.x_cor - 30 < ball.xcor() < brick_8.x_cor + 30:
            brick_8.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_8_existence = False
            bricks += 1
            score += brick_8.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 9
    if brick_9_existence:
        if brick_9.y_cor - 20 < ball.ycor() < brick_9.y_cor + 20 and brick_9.x_cor - 30 < ball.xcor() < brick_9.x_cor + 30:
            brick_9.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_9_existence = False
            bricks += 1
            score += brick_9.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 10
    if brick_10_existence:
        if brick_10.y_cor - 20 < ball.ycor() < brick_10.y_cor + 20 and brick_10.x_cor - 30 < ball.xcor() < brick_10.x_cor + 30:
            brick_10.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_10_existence = False
            bricks += 1
            score += brick_10.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 11
    if brick_11_existence:
        if brick_11.y_cor - 20 < ball.ycor() < brick_11.y_cor + 20 and brick_11.x_cor - 30 < ball.xcor() < brick_11.x_cor + 30:
            brick_11.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_11_existence = False
            bricks += 1
            score += brick_11.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 12
    if brick_12_existence:
        if brick_12.y_cor - 20 < ball.ycor() < brick_12.y_cor + 20 and brick_12.x_cor - 30 < ball.xcor() < brick_12.x_cor + 30:
            brick_12.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_12_existence = False
            bricks += 1
            score += brick_12.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 13
    if brick_13_existence:
        if brick_13.y_cor - 20 < ball.ycor() < brick_13.y_cor + 20 and brick_13.x_cor - 30 < ball.xcor() < brick_13.x_cor + 30:
            brick_13.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_13_existence = False
            bricks += 1
            score += brick_13.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 14
    if brick_14_existence:
        if brick_14.y_cor - 20 < ball.ycor() < brick_14.y_cor + 20 and brick_14.x_cor - 30 < ball.xcor() < brick_14.x_cor + 30:
            brick_14.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_14_existence = False
            bricks += 1
            score += brick_14.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 15
    if  brick_15_existence:
        if brick_15.y_cor - 20 < ball.ycor() < brick_15.y_cor + 20 and brick_15.x_cor - 30 < ball.xcor() < brick_15.x_cor + 30:
            brick_15.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_15_existence = False
            bricks += 1
            score += brick_15.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 16
    if brick_16_existence:
        if brick_16.y_cor - 20 < ball.ycor() < brick_16.y_cor + 20 and brick_16.x_cor - 30 < ball.xcor() < brick_16.x_cor + 30:
            brick_16.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_16_existence = False
            bricks += 1
            score += brick_16.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 17
    if brick_17_existence:
        if brick_17.y_cor - 20 < ball.ycor() < brick_17.y_cor + 20 and brick_17.x_cor - 30 < ball.xcor() < brick_17.x_cor + 30:
            brick_17.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_17_existence = False
            bricks += 1
            score += brick_17.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 18
    if brick_18_existence:
        if brick_18.y_cor - 20 < ball.ycor() < brick_18.y_cor + 20 and brick_18.x_cor - 30 < ball.xcor() < brick_18.x_cor + 30:
            brick_18.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_18_existence = False
            bricks += 1
            score += brick_18.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 19
    if brick_19_existence:
        if brick_19.y_cor - 20 < ball.ycor() < brick_19.y_cor + 20 and brick_19.x_cor - 30 < ball.xcor() < brick_19.x_cor + 30:
            brick_19.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_19_existence = False
            bricks += 1
            score += brick_19.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 20
    if brick_20_existence:
        if brick_20.y_cor - 20 < ball.ycor() < brick_20.y_cor + 20 and brick_20.x_cor - 30 < ball.xcor() < brick_20.x_cor + 30:
            brick_20.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_20_existence = False
            bricks += 1
            score += brick_20.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 21
    if brick_21_existence:
        if brick_21.y_cor - 20 < ball.ycor() < brick_21.y_cor + 20 and brick_21.x_cor - 30 < ball.xcor() < brick_21.x_cor + 30:
            brick_21.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_21_existence = False
            bricks += 1
            score += brick_21.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 22
    if brick_22_existence:
        if brick_22.y_cor - 20 < ball.ycor() < brick_22.y_cor + 20 and brick_22.x_cor - 30 < ball.xcor() < brick_22.x_cor + 30:
            brick_22.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_22_existence = False
            bricks += 1
            score += brick_22.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 23
    if brick_23_existence:
        if brick_23.y_cor - 20 < ball.ycor() < brick_23.y_cor + 20 and brick_23.x_cor - 30 < ball.xcor() < brick_23.x_cor + 30:
            brick_23.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_23_existence = False
            bricks += 1
            score += brick_23.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 24
    if brick_24_existence:
        if brick_24.y_cor - 20 < ball.ycor() < brick_24.y_cor + 20 and brick_24.x_cor - 30 < ball.xcor() < brick_24.x_cor + 30:
            brick_24.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_24_existence = False
            bricks += 1
            score += brick_24.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Brick 25
    if brick_25_existence:
        if brick_25.y_cor - 20 < ball.ycor() < brick_25.y_cor + 20 and brick_25.x_cor - 30 < ball.xcor() < brick_25.x_cor + 30:
            brick_25.disappear()
            ball.dx *= -1
            ball.dy *= -1
            brick_25_existence = False
            bricks += 1
            score += brick_25.point
            pen_score.clear()
            pen_score.write(f"Score: {score}", align="center", font=("Courier", 12, "normal"))

    # Game wining
    if lives > 0 and bricks == 25:
        ball.hideturtle()
        paddle.hideturtle()
        pen_score.clear()
        pen_lives.clear()
        pen_other.setposition(0,0)
        pen_other.write("You win", align="center", font=("Courier", 24, "normal"))
        pen_other.setposition(0,-50)
        pen_other.write(f"Score = {score}", align="center", font=("Courier", 12, "normal"))

    if lives == 0:
        ball.hideturtle()
        paddle.hideturtle()
        pen_other.setposition(0, 0)
        pen_other.write("You Lose", align="center", font=("Courier", 24, "normal"))
