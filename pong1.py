import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @duskzt")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
pointsA=0
pointsB=0


#Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("indigo")
pad_a.shapesize(stretch_wid=5, stretch_len=0.7)
pad_a.penup()
pad_a.goto(-350, 0)

#Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("sky blue")
pad_b.shapesize(stretch_wid=5, stretch_len=0.7)
pad_b.penup()
pad_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("gold")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25
 
#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player 1   {pointsA} X {pointsB}   Player 2", align="center", font=("Courier",24, "normal"))

#Functions
#Paddle A
def paddle_a_up():
    y = pad_a.ycor()
    y+=20
    pad_a.sety(y)

def paddle_a_down():
    y = pad_a.ycor()
    y-=20
    pad_a.sety(y)

#Paddle B
def paddle_b_up():
    y = pad_b.ycor()
    y+=20
    pad_b.sety(y)

def paddle_b_down():
    y = pad_b.ycor()
    y-=20
    pad_b.sety(y)


#Key_binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        #ball.sety(290)
        ball.dy*= -1

    if ball.ycor() < -290:
        ball.dy*=-1

    if ball.xcor() > 390:
        winsound.PlaySound("rebot.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        pointsA+=1
        pen.clear()
        pen.write(f"Player 1   {pointsA} X {pointsB}   Player 2", align="center", font=("Courier",24, "normal"))
        
    
    if ball.xcor() < -390:
        winsound.PlaySound("rebot.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx*= -1
        pointsB+=1
        pen.clear()
        pen.write(f"Player 1   {pointsA} X {pointsB}   Player 2", align="center", font=("Courier",24, "normal"))

    #Paddle and ball collisions
    if ball.xcor()>340 and ball.xcor() < 350 and ball.ycor()<pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor()<-340 and ball.xcor()<-350 and ball.ycor()<pad_a.ycor()+40 and ball.ycor() > pad_a.ycor() -40:
        ball.setx(-340)
        ball.dx*=-1