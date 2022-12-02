from turtle import Turtle

p1_segments = []


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350,0)


    def p1_up(self):
        self.forward(20)
