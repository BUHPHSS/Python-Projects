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

    def __init__(self, x_cor, y_cor, point, color):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.point = point
        self.exist = True
        self.turtle_object = turtle.Turtle()
        self.turtle_object.speed(0)
        self.turtle_object.shape("square")
        self.turtle_object.color("black", color)
        self.turtle_object.shapesize(stretch_wid=1, stretch_len=3)
        self.turtle_object.penup()
        self.turtle_object.goto(x_cor, y_cor)


# Bricks
bricks_obj = []
for y_cors in range(70,151,20):
    for x_cors in range(-120,121,60):
        bricks_obj.append(Brick(x_cors, y_cors, 10, "white"))

red_bricks = [3,11,22]
for brick in red_bricks:
    bricks_obj[brick].point = 20
    bricks_obj[brick].turtle_object.color("black", "red")


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


    # Bricks and ball collision
    for brick in bricks_obj:
        if brick.exist:
            if brick.y_cor - 20 < ball.ycor() < brick.y_cor + 20 and brick.x_cor - 30 < ball.xcor() < brick.x_cor + 30:
                brick.turtle_object.hideturtle()
                ball.dx *= -1
                ball.dy *= -1
                brick.exist = False
                bricks += 1
                score += brick.point
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
