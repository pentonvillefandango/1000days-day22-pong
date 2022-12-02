from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
# screen.tracer(0)
screen.listen()
paddle1 = Paddle()

screen.onkey(paddle1.p1_up(),"Up")














screen.exitonclick()